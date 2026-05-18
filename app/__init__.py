from flask import Flask
from app.config import Config
from app.database.db import db

def create_app():                   # Flask App Factory

    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)

    return app