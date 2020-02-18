from app import db

class Product(db.Model):
    """
    Table schema
    """

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.Float)
    product_name = db.Column(db.String(60))
    size = db.Column(db.String(10))