from flask import Blueprint, request, jsonify, g

from app.database.db import db

from app.models.cart_model import CartItem
from app.models.product_model import Product

from app.utils.auth_decorator import user_required

# ADD TO CART
cart_bp = Blueprint("cart", __name__)
@cart_bp.route("/cart/add", methods=["POST"])
@user_required
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
    
    # Проверка введенного количества
    if quantity > product.stock:
        return jsonify({
            "error": "Not enough stock available"
        }), 400

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

# Get current user's shopping cart
@cart_bp.route("/cart", methods=["GET"])
@user_required
def get_cart():

    cart_items = CartItem.query.filter_by(
        user_id=g.user_id                   # только корзина текущего пользователя
    ).all()

    result = []

    for item in cart_items:
        
        product = Product.query.get(item.product_id)

        result.append({
            "cart_item_id": item.id,
            "product_id": product.id,
            "brand": product.brand,
            "model": product.model,
            "price": product.price,
            "quantity": item.quantity
        })   

    return jsonify(result), 200

# REMOVE FROM CART
@cart_bp.route("/cart/remove/<int:cart_item_id>", methods=["DELETE"])
@user_required
def remove_from_cart(cart_item_id):

    cart_item = CartItem.query.filter_by(
        id=cart_item_id,
        user_id=g.user_id
    ).first()

    # Проверка существования
    if not cart_item:
        return jsonify({
            "ERROR": "Cart item not found"
        }), 404
    
    db.session.delete(cart_item)

    db.session.commit()

    return jsonify({
        "MESSAGE": "Item removed from cart"
    }), 200
