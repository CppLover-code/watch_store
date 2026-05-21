from flask import Blueprint, jsonify, g

from app.database.db import db

from app.models.cart_model import CartItem
from app.models.product_model import Product
from app.models.order_model import Order
from app.models.order_item_model import OrderItem

from app.utils.auth_decorator import user_required

order_bp = Blueprint("orders", __name__)
# CHECKOUT
