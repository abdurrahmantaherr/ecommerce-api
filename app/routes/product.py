from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.product import Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators import admin_required

product_bp = Blueprint("product", __name__)

@product_bp.route("/product", methods = ['POST'])
@jwt_required()
@admin_required
def create_product():

    user_id = get_jwt_identity()

    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    if not name or price is None or stock is None:
        return jsonify({
            "error":"Missing field required!"
        }),400
    
    product = Product(
        name = name,
        description = description,
        price = price,
        stock = stock,
        user_id = user_id
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message":"Product created successfully"
    }),200

@product_bp.route('/product', methods=["GET"])
def get_products():

    #products  = Product.query.all()
    query = Product.query

    page = request.args.get("page", 1, type = int)
    per_page = request.args.get("per_page", 5, type=int)

    name = request.args.get("name")
    min_price = request.args.get("min_price", type = float)
    max_price = request.args.get("max_price", type = float)
    
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if min_price is not None:
        query = query.filter(Product.price>=min_price)
    if max_price is not None:
        query = query.filter(Product.price<=max_price)


    pagination = query.paginate(
        page = page,
        per_page = per_page,
        error_out=False
    )

    product_list = []

    for product in pagination.items:
        product_list.append({
            "id":product.id,
             "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock
            
        })


    return jsonify({
        "products": product_list,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total_products": pagination.total,
        "total_pages": pagination.pages
    }), 200

@product_bp.route("/product/<int:id>", methods = ["GET"])
def get_product(id):

    product = Product.query.get(id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404
    
    return jsonify({

        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock

    }),200

@product_bp.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
   
    
    product = Product.query.get(id)

    if not product:
        return jsonify({
            "error":"Product not found"
        }), 404
    data  = request.get_json()

    product.name = data.get("name")
    product.description = data.get("description")
    product.price = data.get("price")
    product.stock = data.get("stock")

    
    db.session.commit()

    return jsonify({
        "message":"Product updated successfully"
    }), 200

@product_bp.route("/product/<int:id>", methods = ["DELETE"])
def delete_product(id):

    product = Product.query.get(id)

    if not product:
        return jsonify({
            "error":"Product not found"
        }), 404
    
    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message":"Product deleted successfully"
    }), 200