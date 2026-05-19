from app.database.db import db
from app.models.product_model import Product

# список товаров - список словарей
products = [
    {
        "brand": "Rolex",
        "model": "Submariner",
        "price": 12000,
        "description": "Luxury diving watch",
        "image_url": "",
        "stock": 5
    },

    {
        "brand": "Omega",
        "model": "Speedmaster",
        "price": 7500,
        "description": "Moonwatch chronograph",
        "image_url": "",
        "stock": 3
    },

    {
        "brand": "Casio",
        "model": "G-Shock",
        "price": 120,
        "description": "Durable sports watch",
        "image_url": "",
        "stock": 15
    },

    {
        "brand": "Tissot",
        "model": "PRX",
        "price": 650,
        "description": "Modern classic watch",
        "image_url": "",
        "stock": 10
    },

    {
        "brand": "Seiko",
        "model": "Presage",
        "price": 900,
        "description": "Japanese automatic watch",
        "image_url": "",
        "stock": 7
    }
]

def seed_products():

    existing_products = Product.query.first()   # protection against re-adding products

    if existing_products:
        print("Products already seeded")
        return
    
    for item in products:

        product = Product(
            brand=item["brand"],
            model=item["model"],
            price=item["price"],
            description=item["description"],
            image_url=item["image_url"],
            stock=item["stock"]
        )

        db.session.add(product)

    db.session.commit()

    print("Products seeded successfully")