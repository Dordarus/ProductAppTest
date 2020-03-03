import json
from flask import Response
from . import health
from flasgger import swag_from
from logs import log_file_path

@health.route('/health', methods=['GET'])
@swag_from('../../docs/health_doc.yml')
def health():
    with open(log_file_path, 'r') as logs:
        log_lines_json = [json.loads(x) for x in logs.readlines()]
    
    return Response(json.dumps(log_lines_json),  mimetype='application/json')