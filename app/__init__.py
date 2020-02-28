import os
import logging
from logs import file_handler, logging_level

from .config import app_config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flasgger import Swagger
from docs import template


environment = os.environ.get('FLASK_ENV')

app = Flask(__name__, static_folder=None)
app.config.from_object(app_config[environment])

app.logger.addHandler(file_handler)
app.logger.setLevel(logging_level)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

seeder = FlaskSeeder()
seeder.init_app(app, db)

from . import views, models

from app.product import product
app.register_blueprint(product, url_prefix='/api/v1')

from app.health import health
app.register_blueprint(health)

Swagger(app, template=template)