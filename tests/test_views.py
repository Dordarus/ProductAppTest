from tests.base import BaseTestCase, json
from app.models import Product
import unittest

class TestViews(BaseTestCase):
    def test_show_with_right_product_id(self):
        product_id = 132456
        product = Product.get_by_id(product_id)

        with self.client:
            response = self.client.get(f'/api/v1/products/{product_id}')
            data = json.loads(response.data.decode())

        self.assertEqual(data['product_id'],  product.product_id)
        self.assertEqual(data['product_name'],  product.product_name)
        self.assertEqual(data['product_price'],  product.product_price)
        self.assertEqual(data['size'],  product.size)

    def test_show_with_wrong_product_id(self):
        product_id_with_letters = 'abc'
        product_id_with_not_exist_number = 42
        blank_product_id = None

        with self.client:
            response_with_letter = self.client.get(f'/api/v1/products/{product_id_with_letters}')       
            response_with_not_exist = self.client.get(f'/api/v1/products/{product_id_with_not_exist_number}')
            response_with_blank = self.client.get(f'/api/v1/products/{blank_product_id}')

        self.assertEqual(response_with_letter.status_code, 404)
        self.assertEqual(response_with_not_exist.status_code, 404)
        self.assertEqual(response_with_blank.status_code, 404)

if __name__ == '__main__':
    unittest.main()