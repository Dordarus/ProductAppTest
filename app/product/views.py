from flask import make_response, jsonify
from app.models import Product
from . import product

# TODO: Refactor requests to helpers
@product.route('/products/<product_id>', methods=['GET'])
def show(product_id):
    """
    Return a product with the supplied product Id.
    :param product_id: Product Id
    :return:
    """

    try:
        int(product_id)
    except ValueError:
        return make_response(jsonify({
            'message': "Use valid product id"
        })), 422
    else:
        product = Product.get_by_id(product_id)

        if product:
            return make_response(
                jsonify(
                    product.json()
                )
            ), 200
        else:
            return make_response(jsonify({
                'message': "Product with id=%s doesn`t exist" % product_id
            })), 404
        
