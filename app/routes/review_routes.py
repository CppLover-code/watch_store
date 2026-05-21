from flask import Blueprint, request, jsonify, g

from datetime import datetime

from app.database.mongo import reviews_collection

from app.models.product_model import Product

from app.utils.auth_decorator import user_required

review_bp = Blueprint("reviews", __name__)

@review_bp.route("/reviews", methods=["POST"])
@user_required
def create_review():

    data = request.get_json()

    product_id = data.get("product_id")
    rating = data.get("rating")
    comment = data.get("comment")

    # Проверка товара
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "ERROR": "Product not found"
        }), 404
    
    review = {
        "product_id": product_id,
        "user_id": g.user_id,
        "rating": rating,
        "comment": comment,
        "created_at": datetime.utcnow()
    }

    reviews_collection.insert_one(review)

    return jsonify({
        "MESSAGE": "Review added successfully"
    }), 201