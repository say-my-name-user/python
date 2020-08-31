import json, datetime
from src import __version__
from flask import session
from time import time


class Response:
    codes = {
        'OK'                   : 200,
        'BAD_REQUEST'          : 400,
        'NOT_FOUND'            : 404,
        'INTERNAL_SERVER_ERROR': 500,
    }

    def __init__(self, data='[]'):
        self.data = data

    def json(self):
        return json.dumps({
            'status' : True,
            'data'   : self.data,
            'api'    : 'v{}'.format(__version__),
            'latency': round(time() - session.get('start_time'), 3)
        }, default=self.custom_converter)

    @staticmethod
    def custom_converter(o):
        """Convert unusual data types to string during JSON encoding"""

        if isinstance(o, datetime.date):
            return o.__str__()

    @staticmethod
    def not_found():
        return json.dumps({'status': False, 'message': 'Method not found'}), Response.codes['NOT_FOUND']

    @staticmethod
    def internal_server_error(e):
        return json.dumps({'status': False, 'message': str(e)}), Response.codes['INTERNAL_SERVER_ERROR']
