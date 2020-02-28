from tests.base import BaseTestCase
from app.models import Product
from tests.helpers import get_last_log_record
import unittest, json

class TestErrorHandlersWithLogging(BaseTestCase):

    def test_pagenotfound_statuscode(self):
        with self.client:
            response = self.client.get('/missing_page')

        self.assertEqual(response.status_code, 404) 

    def test_pagenotfound_data(self):
        with self.client:
            response = self.client.get('/missing_page')

        data = json.loads(response.data.decode())

        self.assertIn('[404 Not Found]', data['message'])

    def test_pagenotfound_logs(self):
        response = self.client.get('/missing_page')
        data = json.loads(response.data.decode())

        last_log_dict = get_last_log_record()

        self.assertEqual(data['message'], last_log_dict['message']) 

    def test_unhandledexception_statuscode(self):
        with self.client:
            response = self.client.get('api/v1/products/500')

        self.assertEqual(response.status_code, 500) 

    def test_unhandledexception_data(self):
        with self.client:
            response = self.client.get('api/v1/products/500')

        data = json.loads(response.data.decode())

        self.assertIn('[500 Internal Server Error]', data['message'])

    def test_unhandledexception_logs(self):
        response = self.client.get('api/v1/products/500')
        data = json.loads(response.data.decode())

        last_log_dict = get_last_log_record()

        self.assertEqual(data['message'], last_log_dict['message']) 

    def test_success_logs(self):
        product = Product.query.first()

        with self.client:
            response = self.client.get(f'/api/v1/products/{product.product_id}')
            data = json.loads(response.data.decode())

        last_log_dict = get_last_log_record()

        self.assertEqual("200 OK", last_log_dict['message']) 

if __name__ == '__main__':
    unittest.main()