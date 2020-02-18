import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import app_config

environment = os.environ.get('FLASK_ENV')

app = Flask(__name__, static_folder=None)
app.config.from_object(app_config[environment])

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views, models

from app.product import product
app.register_blueprint(product, url_prefix='/v1')


