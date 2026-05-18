from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt

from app.database.db import db
from app.models.user_model import User

from app.utils.jwt_handler import create_token

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

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # checking a user
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "ERROR": "Invalid email or password"
        }), 401
    
    # checking a password
    password_correct = bcrypt.check_password_hash(
        user.password,
        password
    )

    if not password_correct:
        return jsonify({
            "ERROR": "Invalid email or password"
        }),401
    
    # JWT creating
    token = create_token(user.id)

    return jsonify({
        "MESSAGE": "Login succesful",
        "token": token
    }), 200