from flask import jsonify


def generate_response(status_code: int, data: dict = None):
    status = 'success' if 200 <= status_code <= 299 else 'failure'
    response = {
        'status': status
    }
    if data is not None:
        response['data'] = data
    return jsonify(response), status_code
