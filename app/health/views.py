import json
from flask import Response
from . import health
from logs import log_file_path

@health.route('/health', methods=['GET'])
def health():
    with open(log_file_path, 'r') as logs:
        log_lines_json = [json.loads(x) for x in logs.readlines()]
    
    return Response(json.dumps(log_lines_json),  mimetype='application/json')