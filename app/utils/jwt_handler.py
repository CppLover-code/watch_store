import jwt
import datetime
import os

from dotenv import load_dotenv

load_dotenv()

def create_token(user_id):

    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }

    token = jwt.encode(
        payload,
        os.getenv("JWT_SECRET_KEY"),
        algorithm="HS256"
    )

    return token