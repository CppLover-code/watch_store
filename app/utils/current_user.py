import jwt
import os

from functools import wraps
from flask import request, jsonify, g

from dotenv import load_dotenv

load_dotenv()

# g = глобальный объект Flask, можно положить текущего пользователя.
def login_required(f):

    @wraps(f)
    def decorated(*args,**kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({
                "ERROR": "Token is missing"
            }), 401
        
        try:

            token = auth_header.split(" ")[1]

            decoded = jwt.decode(
                token,
                os.getenv("JWT_SECRET_KEY"),
                algorithms=["HS256"]
            )

            # сохраняем user_id
            g.user_id = decoded["user_id"]
        
        except Exception as e:

            return jsonify({
                "ERROR": "Invalid token",
                "details": str(e)
            }), 401
        
        return f(*args, **kwargs)
    
    return decorated