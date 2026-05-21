# Watch Store API

A full-featured REST API for a watch store built with Flask.

This project includes authentication, authorization, shopping cart logic, checkout system, orders, and MongoDB reviews.

---

# Technologies

- Python
- Flask
- PostgreSQL
- MongoDB
- SQLAlchemy
- Flask-Migrate
- JWT Authentication
- bcrypt
- pymongo

---

# Features

## Authentication

- User registration
- User login
- JWT authentication
- Password hashing with bcrypt

---

## Authorization

- Admin role
- User role
- Protected routes
- Role-based access control

---

## Products

- Create products
- Update products
- Delete products
- Get all products
- Get product by ID

Only admins can manage products.

---

## Shopping Cart

Users can:

- Add products to cart
- View cart
- Remove items from cart

---

## Checkout System

Checkout process:

- Creates orders
- Creates order items
- Decreases product stock
- Clears cart after successful checkout

---

## MongoDB Reviews

Users can:

- Add product reviews
- View product reviews

Reviews are stored in MongoDB.

---

# Project Structure

watch_store/

├── app/

│   ├── database/

│   ├── models/

│   ├── routes/

│   ├── seed/

│   ├── utils/

│   ├── config.py

│   └── __init__.py

│

├── migrations/

├── .env

├── .gitignore

├── requirements.txt

├── run.py

└── README.md

---

# Installation

## Clone repository

```bash
git clone <your_repository_url>
cd watch_store

---
# Create virtual environment
python -m venv .venv

---
Activate virtual environment

Windows
.venv\Scripts\activate

Linux / MacOS
source .venv/bin/activate

---
Install dependencies
pip install -r requirements.txt

---
Environment Variables

Create .env file:

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=watch_store

---
PostgreSQL Setup

Create database:

CREATE DATABASE watch_store;

---
Run Migrations
flask db migrate
flask db upgrade

---
Run Application
py run.py

Server will start at:

http://127.0.0.1:5000

---
API Endpoints

Authentication
Register
POST /register

Login
POST /login

Products
Get all products
GET /products
Get product by ID
GET /products/<id>

Create product
POST /products
Admin only.

Update product
PUT /products/<id>
Admin only.

Delete product
DELETE /products/<id>
Admin only.

Cart
Add to cart
POST /cart/add
View cart
GET /cart
Remove item from cart
DELETE /cart/remove/<id>

Orders
Checkout
POST /checkout

Reviews
Create review
POST /reviews
Get product reviews
GET /reviews/<product_id>

---
Database Architecture
Feature	                Database
Users	                PostgreSQL
Products	            PostgreSQL
Orders	                PostgreSQL
Reviews	                MongoDB

---
Future Improvements:

Swagger/OpenAPI documentation
Product image uploads
Payment integration
Admin dashboard
Product categories
Order history
Email notifications

---
Author

Watch Store API learning project built with Flask.