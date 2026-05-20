import jwt
import os

from functools import wraps                     # нужен для создания decorators
from flask import request, jsonify

from dotenv import load_dotenv

load_dotenv()

def admin_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        # Проверка наличия токена
        if not auth_header:
            return jsonify({
                "error": "Token is missing"
            }), 401

        try:

            # Убираем Bearer
            token = auth_header.split(" ")[1]

            # Декодируем JWT
            decoded = jwt.decode(
                token,
                os.getenv("JWT_SECRET_KEY"),
                algorithms=["HS256"]
            )

            # Проверка роли
            if decoded["role"] != "admin":
                return jsonify({
                    "error": "Admin access required"
                }), 403

        except Exception as e:

            return jsonify({
                "error": "Invalid token",
                "details": str(e)
            }), 401

        return f(*args, **kwargs)

    return decorated