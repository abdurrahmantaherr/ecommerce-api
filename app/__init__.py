from flask import Flask

from app.config import Config
from app.routes.home import home_bp
from app.routes.product import product_bp
from app.routes.auth import auth_bp, login_bp, profile_bp, refresh_bp
from app.extensions import db, migrate, bcrypt, jwt

from app.models.user import User
from app.models.product import Product


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app,db)

    bcrypt.init_app(app)

    jwt.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(refresh_bp)

    return app


