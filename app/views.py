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
  try:
    except_dict = {"code": e.code, "message": f"[{e.code} {e.name}] {e.description}"}
  except AttributeError as ex:
    except_dict = {"code": 500, "message": str(e)}

  app.logger.error(except_dict["message"])

  return make_response(
    jsonify({'message': except_dict["message"]})
  ), except_dict["code"]