import json
from flask_seeder import Seeder
from app.models import Product

class ProductSeeder(Seeder):
    def run(self):
        with open('test.json', 'r') as json_file:
            products = json.load(json_file)
    
        for product in products:
            print("Adding product: %s" % product['product_name'])
            
            # Init Product by unpacked dictionary
            self.db.session.add(Product(**product))

        