# E-Commerce REST API

A secure and scalable RESTful API for an E-Commerce platform built with **Flask**. This project implements authentication using JWT, role-based authorization, CRUD operations, pagination, filtering, and image uploads.

---

## Features

- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ Refresh Tokens
- ✅ Role-Based Authorization (Admin/User)
- ✅ Product CRUD APIs
- ✅ Pagination
- ✅ Product Filtering
- ✅ SQLAlchemy ORM
- ✅ Flask-Migrate Database Migrations
- ✅ Password Hashing using Bcrypt
- ✅ Modular Project Structure

---

## Tech Stack

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask JWT Extended
- Flask Bcrypt
- SQLite
- Postman

---

## 📂 Project Structure

```
ecommerce-api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── extensions.py
│   ├── decorators.py
│   ├── config.py
│   └── __init__.py
│
├── migrations/
├── run.py
├── wsgi.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/abdurrahmantaherr/ecommerce-api.git
```

```bash
cd ecommerce-api
```

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret

DATABASE_URL=sqlite:///instance/ecommerce.db
```

---

## Database Migration

```bash
flask db init
```

```bash
flask db migrate -m "Initial Migration"
```

```bash
flask db upgrade
```

---

## Run the Server

```bash
python run.py
```

or

```bash
flask run
```

Server:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register User |
| POST | /login | Login User |
| POST | /refresh | Generate New Access Token |

---

## Products

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /product | Get All Products |
| GET | /product/<id> | Get Product |
| POST | /product | Create Product (Admin) |
| PUT | /product/<id> | Update Product |
| DELETE | /product/<id> | Delete Product |

---

## Categories

| Method | Endpoint |
|---------|----------|
| GET | /categories |
| POST | /categories |

---

## Orders

| Method | Endpoint |
|---------|----------|
| GET | /orders |
| POST | /orders |

---

## Cart

| Method | Endpoint |
|---------|----------|
| GET | /cart |
| POST | /cart |

---

## Pagination

Example

```
GET /product?page=1&per_page=5
```

---

## Filtering

Example

```
GET /product?min_price=100
```

```
GET /product?max_price=500
```

```
GET /product?name=laptop
```

---

## Authentication

Protected routes require:

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## Database

Tables

- Users
- Products
- Categories
- Orders
- Cart

---

## Testing

The API can be tested using:

- Postman
- Thunder Client

---

## Future Improvements

- PostgreSQL
- Docker
- Redis Token Blacklisting
- Unit Testing
- Swagger Documentation
- CI/CD Pipeline

---

## Author

**Abdurrahman Tahir**

BS Data Science  
University of the Punjab

GitHub

https://github.com/abdurrahmantaherr

LinkedIn

(Add your LinkedIn profile here)

---

## License

This project is developed for educational and portfolio purposes.
## API Testing

This project includes a Postman collection.

Files:

- Ecommerce_API.postman_collection.json
- Local_Development.postman_environment.json

Import both into Postman and use the Login request to generate JWT tokens before testing protected endpoints.
