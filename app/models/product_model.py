from app.database.db import db

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    brand = db.Column(
        db.String(100),
        nullable=False
    )

    model = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    image_url = db.Column(
        db.String(500),
        nullable=True
    )

    stock = db.Column(
        db.Integer,
        default=0
    )
    
    # turn the model into a dictionary because
    # a SQLAlchemy object can't simply be returned as JSON
    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "price": self.price,
            "description": self.description,
            "image_url": self.image_url,
            "stock": self.stock
        }