from flask import make_response, jsonify

def message_response(message, status_code):
    """
    Helper method to make a http response
    :param message: Response message
    :param status_code: Response status code
    :return: Http Response
    """

    return make_response(jsonify({
        'message': message
    })), status_code

def product_response(product):
    """
    Helper method to make a http response with product JSON
    :param product: Product object
    :return: Http Response
    """

    return make_response(
        jsonify(
            product.json()
        )
    ), 200

