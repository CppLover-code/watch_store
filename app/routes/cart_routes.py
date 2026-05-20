from flask import Blueprint, request, jsonify, g

from app.database.db import db

from app.models.cart_model import CartItem
from app.models.product_model import Product

from app.utils.current_user import login_required

# ADD TO CART
cart_bp = Blueprint("cart", __name__)
@cart_bp.route("/cart/add", methods=["POST"])
@login_required
def add_to_cart():

    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    # Проверка товара
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "ERROR": "Product not found"
        }), 404
    
    # Проверка существования в корзине
    existing_item = CartItem.query.filter_by(
        user_id=g.user_id,
        product_id=product_id
    ).first()

    # если товар уже есть
    if existing_item:

        existing_item.quantity += quantity

    else:

        cart_item = CartItem(
            user_id=g.user_id,
            product_id=product_id,
            quantity=quantity
        )
        
        db.session.add(cart_item)
    db.session.commit()

    return jsonify({
        "MESSAGE": "Product added to cart"
    }), 201