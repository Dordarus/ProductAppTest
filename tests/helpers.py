import json
from logs import log_file_path

def get_last_log_record():
    with open(log_file_path, 'r') as logs:
            last_log_line = logs.readlines()[-1]

    return json.loads(last_log_line)