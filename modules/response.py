import json
import datetime


class Response:
    def __init__(self, data=None):
        self.data = data

    @staticmethod
    def date_converter(o):
        if isinstance(o, datetime.date):
            return o.__str__()

    def encode(self):
        return json.dumps(self.data, default=self.date_converter)

    @staticmethod
    def not_found():
        return json.dumps({'status': False, 'message': 'Method not found'})

    @staticmethod
    def internal_server_error(e):
        return json.dumps({'status': False, 'message': str(e)})
