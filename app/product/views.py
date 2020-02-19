from .helper import message_response, product_response
from app.models import Product
from . import product

@product.route('/products/<product_id>', methods=['GET'])
def show(product_id):
    """
    Return a product with the supplied product Id.
    :param product_id: Product Id
    :return:
    """

    product = Product.get_by_id(product_id)

    if product:
        return product_response(product)
    else:
        return message_response(
            f"Product with id={product_id} doesn`t exist",
            404
        )
        
