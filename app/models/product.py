from app.extensions import db

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(500), nullable = True)

    description = db.Column(db.Text)

    price = db.Column(db.Float, nullable = True )

    stock = db.Column(db.Integer, default = 0)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
