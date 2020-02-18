from flask import make_response, jsonify

from . import product

@product.route('/products', methods=['GET'])
def index():
    """
    """
    return make_response(jsonify({
        'message': 'Working good!'
    })), 200