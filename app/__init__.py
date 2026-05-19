from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config import Config
from app.database.db import db

from app.models.user_model import User
from app.models.product_model import Product

from app.routes.auth_routes import auth_bp


migrate = Migrate()
bcrypt = Bcrypt()

def create_app():                   # Flask App Factory

    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app,db)

    bcrypt.init_app(app)

    # Blueprint registration
    app.register_blueprint(auth_bp)

    return app