import time
from . import app
from flask import g
from werkzeug.exceptions import InternalServerError

@app.before_request
def before_request():
  g.start = time.time()

@app.after_request
def after_request(response):
    level_dict = {200: 'info', 404: 'warning'}
    logger_obj = getattr(app.logger, level_dict[response.status_code])
    logger_obj(response.status)
    return response

@app.errorhandler(InternalServerError)
def handle_500(e):
    app.logger.error(e, exc_info=None)
    return e