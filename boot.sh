#!/bin/bash

export FLASK_ENV=production
gunicorn --chdir app app:app -w 2 --threads 2 -b 0.0.0.0:5000