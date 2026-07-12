from flask import Blueprint, jsonify, request
from app.models.user import User
from app.extensions import bcrypt, db
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token, 
    get_jwt_identity, 
    jwt_required
)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods = ['POST'])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "message":"Missing field!"
        }), 400
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already registered!"
        }), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        username = username,
        email = email,
        password = hashed_password
    )

    db.session.add(new_user)
    db.session.commit()
    


    return jsonify({
        "message": "User is Registered Successfully"
    }), 201


login_bp = Blueprint("login", __name__)

@login_bp.route('/login', methods = ["POST"])
def verify():

    data  = request.get_json()

    
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "Error" : "email and pasword required"
        }),400
    
    user  = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "Error" : "Invalid username or password"
        })
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({
            "Error" : "Invalid username or password"
        })
    
    access_token = create_access_token(identity= str(user.id))
    refresh_token = create_refresh_token(identity = str(user.id))

    return jsonify({
        "access_token": access_token ,
        "refresh_token": refresh_token
    }), 201

refresh_bp = Blueprint("refresh", __name__)
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():

    user_id = get_jwt_identity()

    access_token = create_access_token(identity=user_id)

    return jsonify({
        "access_token": access_token
    }), 200

profile_bp = Blueprint("profile", __name__)
@profile_bp.route('/profile')
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = User.query.get(int(user_id))

    if not user:
        return jsonify({
            "error":"User not found"
        }), 404

    return jsonify({
        "message": "Protected route access granted",
        "user ID": user_id,
        "username": user.username,
        "email": user.email
    }), 200
        
    