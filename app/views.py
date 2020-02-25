import time
from . import app
from flask import g, make_response, jsonify

@app.before_request
def before_request():
  g.start = time.time()

@app.after_request
def after_request(response):
  if response.status_code == 200:
    app.logger.info(response.status)

  return response

@app.errorhandler(Exception)
def unhandled_exception(e):
  error_desc = f"[{e.code} {e.name}] {e.description}"

  app.logger.error(error_desc)

  return make_response(
    jsonify({'message': error_desc})
  ), e.code