from flask import Blueprint, jsonify, request

from app.models.product_model import Product

from app.database.db import db

from app.utils.auth_decorator import admin_required

product_bp = Blueprint("products", __name__)

# GET ALL PRODUCTS
@product_bp.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()              # получаем список объектов

    products_list = []

    for product in products:
        products_list.append(product.to_dict()) # превращаем объект в обычный Python dict

    return jsonify(products_list), 200          # превращает список dict → JSON.

# GET PRODUCT BY ID
@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "ERROR": "Product not found"
        }), 404
    
    return jsonify(product.to_dict()), 200

# Adding a product
@product_bp.route("/products", methods=["POST"])
@admin_required                                     # проверка роли админа
def create_product():

    data = request.get_json()                       # Получаем JSON из POST запроса.

    # безопасно достаем поля
    brand = data.get("brand")
    model = data.get("model")
    price = data.get("price")
    description = data.get("description")
    image_url = data.get("image_url")
    stock = data.get("stock")

    # Проверка обязательных полей
    if not brand or not model or not price:
        return jsonify({
            "ERROR": "Missing required fields"
        }), 400
    
    # Создание объекта
    new_product = Product(
        brand=brand,
        model=model,
        price=price,
        description=description,
        image_url=image_url,
        stock=stock
    )

    # Сохранение в БД
    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "MESSAGE": "Product created successfully",
        "product": new_product.to_dict()
    }),201
