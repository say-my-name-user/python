import json
import datetime
from src import __version__
from flask import session
from time import time


class Wrapper:
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
