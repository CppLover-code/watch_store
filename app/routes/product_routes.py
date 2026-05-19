from flask import Blueprint, jsonify

from app.models.product_model import Product

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