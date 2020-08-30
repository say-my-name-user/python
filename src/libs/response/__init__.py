import json


codes = {
    'OK'                   : 200,
    'BAD_REQUEST'          : 400,
    'NOT_FOUND'            : 404,
    'INTERNAL_SERVER_ERROR': 500,
}


def not_found():
    return json.dumps({'status': False, 'message': 'Method not found'}), codes['NOT_FOUND']


def internal_server_error(e):
    return json.dumps({'status': False, 'message': str(e)}), codes['INTERNAL_SERVER_ERROR']
