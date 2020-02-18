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

    @staticmethod
    def get_by_id(product_id):
        """
        Check a product by their product ids
        :param product_id:
        :return:
        """
        return Product.query.filter_by(product_id = product_id).first()

    def json(self):
        """
        Json representation of the product model.
        :return:
        """
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'size': self.size
        }