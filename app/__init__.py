import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config

environment = os.environ.get('FLASK_ENV')

app = Flask(__name__, static_folder=None)

db = SQLAlchemy(app)

app.config.from_object(app_config[environment])

