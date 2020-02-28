import json, os
from logs import log_file_path
from app import app, db
from flask import Flask
from app.models import Product
from flask_testing import TestCase
from app.config import app_config

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(app_config['test'])
        return app

    def setUp(self):
        db.create_all()
        self._seed_db()
        # Create test env log file and clear it on each test
        open(log_file_path, 'w')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _seed_db(self):
        with open('test.json', 'r') as json_file:
            products = json.load(json_file)
    
        for product in products:
            print("Adding product: %s" % product['product_name'])
            
            # Init Product by unpacked dictionary
            db.session.add(Product(**product))

    
    