from functools import wraps

from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from app.models.user import User

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        user_id = get_jwt_identity()
        user = User.query.get(int(user_id))

        if not user:
            return jsonify({
                "error":"User not found."
            }),404
        
        if user.role!="admin":
            return jsonify({
                "error":"Admin access required!"
            }),403
        
        return func(*args, **kwargs)
    
    return wrapper


       