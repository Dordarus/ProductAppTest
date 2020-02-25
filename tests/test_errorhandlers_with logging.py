from tests.base import BaseTestCase, json
from app.models import Product
import unittest

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

    # def test_pagenotfound_logs(self):
    #     result = self.app.get('/missing-page') 

    #     self.assertEqual(result.status_code, 404) 

    # def test_unhandledexception_statuscode(self):
    #     result = self.app.get('/products') 

    #     self.assertEqual(result.status_code, 500) 

    # def test_unhandledexception_data(self):
    #     result = self.app.get('/products') 

    #     self.assertIn('Something Went Wrong', result.data)

    # def test_unhandledexception_logs(self):
    #     result = self.app.get('/missing-page') 

    #     self.assertEqual(result.status_code, 404) 

    # def test_success_statuscode(self):
    #     result = self.app.get('/products') 

    #     self.assertEqual(result.status_code, 500) 

    # def test_success_data(self):
    #     result = self.app.get('/products') 

    #     self.assertIn('Something Went Wrong', result.data)

    # def test_success_data(self):
    # result = self.app.get('/products') 

    # self.assertIn('Something Went Wrong', result.data)

if __name__ == '__main__':
    unittest.main()