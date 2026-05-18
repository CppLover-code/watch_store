from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt

from app.database.db import db
from app.models.user_model import User

auth_bp = Blueprint("auth", __name__)

bcrypt = Bcrypt()

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()                           # Gets JSON from a POST request.

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # checking empty fields
    if not username or not email or not password:
        return jsonify({
            "ERROR": "All fields are required"
        }), 400
    
    # checking an existing user
    existing_user = User.query.filter(
        (User.username == username) |
        (User.email == email)
    ).first()

    if existing_user:
        return jsonify({
            "ERROR": "User already exists"
        }),409

    # password Hashing
    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    # creating a user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    # saving in database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered succesfully"
    }), 201