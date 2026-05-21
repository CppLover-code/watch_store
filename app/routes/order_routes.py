from flask import Blueprint, jsonify, g

from app.database.db import db

from app.models.cart_model import CartItem
from app.models.product_model import Product
from app.models.order_model import Order
from app.models.order_item_model import OrderItem

from app.utils.auth_decorator import user_required

order_bp = Blueprint("orders", __name__)
# CHECKOUT
@order_bp.route("/checkout", methods=["POST"])
@user_required
def checkout():

    # Получаем корзину пользователя
    cart_items = CartItem.query.filter_by(
        user_id=g.user_id
    ).all()

    # Проверка пустой корзины
    if not cart_items:
        return jsonify({
            "ERROR": "Cart is empty"
        }), 400
    
    total_price = 0

    # Считаем сумму заказа
    for item in cart_items:

        product = Product.query.get(item.product_id)

        # проверка stock
        if item.quantity > product.stock:
            return jsonify({
                "ERROR": f"Not enough stock for {product.model}"
            }), 400
        
        total_price += product.price * item.quantity

    # создаем order
    order = Order(
        user_id=g.user_id,
        total_price=total_price
    )

    db.session.add(order)

    # commit нужен, чтобы появился order.id
    db.session.commit()

    # создаем order_items
    for item in cart_items:

        product = Product.query.get(item.product_id)

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price
        )

        db.session.add(order_item)

        # уменьшаем stock
        product.stock -= item.quantity

    # очищаем корзину
    for item in cart_items:
        db.session.delete(item)

    db.session.commit()

    return jsonify({
        "message": "Checkout successful",
        "order_id": order.id,
        "total_price": total_price
    }), 201
