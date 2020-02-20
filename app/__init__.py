import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flasgger import Swagger
from docs import template

from .config import app_config

environment = os.environ.get('FLASK_ENV')

app = Flask(__name__, static_folder=None)
app.config.from_object(app_config[environment])

db = SQLAlchemy(app)

migrate = Migrate(app, db)

seeder = FlaskSeeder()
seeder.init_app(app, db)

from app import views, models

from app.product import product
app.register_blueprint(product, url_prefix='/api/v1')

Swagger(app, template=template)