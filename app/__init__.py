from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config import Config
from app.database.db import db

from app.models.user_model import User
from app.models.product_model import Product
from app.models.cart_model import CartItem
from app.models.order_model import Order
from app.models.order_item_model import OrderItem

from app.routes.auth_routes import auth_bp
from app.routes.product_routes import product_bp
from app.routes.cart_routes import cart_bp
from app.routes.order_routes import order_bp
from app.routes.review_routes import review_bp

from app.seed.products_seed import seed_products


migrate = Migrate()
bcrypt = Bcrypt()

def create_app():                   # Flask App Factory

    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app,db)

    with app.app_context():
        seed_products()

    bcrypt.init_app(app)

    # Blueprint registration
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(review_bp)

    return app