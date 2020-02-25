import time, os
from app.config import app_config
from logging import Formatter, Filter, INFO
from logging.handlers import RotatingFileHandler
from flask import has_request_context, request, g

environment = os.environ.get('FLASK_ENV')
log_file_path = app_config[environment].LOG_FILE

class RequestFormatter(Formatter):
    """Add duration and url attributes to Formatter object"""
    def format(self, record):
        record.url = None
        record.duration = None

        if has_request_context():
            record.url = request.url
            record.duration = time.time() - g.start

        return super().format(record)

file_formatter = RequestFormatter(
    "{'time':'%(asctime)s', 'name': '%(name)s', \
    'level': '%(levelname)s', 'message': '%(message)s',\
    'duration': '%(duration)s', 'url':'%(url)s'},"
)

class TracebackInfoFilter(Filter):
    """Clear or restore the exception on log records"""
    def __init__(self, clear=True):
        self.clear = clear
    def filter(self, record):
        if self.clear:
            record._exc_info_hidden, record.exc_info = record.exc_info, None
            # clear the exception traceback text cache, if created.
            record.exc_text = None
        elif hasattr(record, "_exc_info_hidden"):
            record.exc_info = record._exc_info_hidden
            del record._exc_info_hidden
        return True

logging_level = INFO
file_handler = RotatingFileHandler(log_file_path)
file_handler.setFormatter(file_formatter)
file_handler.addFilter(TracebackInfoFilter())
file_handler.setLevel(logging_level)