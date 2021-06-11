import requests
import json
from src import config
from datetime import date


class PushNotificationsClient:
    @staticmethod
    def send_notification(user_token: str):
        notification = {
            'data': {
                'notification': {
                    'title': 'Hello',
                    'body': 'How are you?'
                 }
            },
           'to': user_token
        }

        response = requests.post(
            url=config.get('API', 'FIREBASE_NOTIFICATION_ENDPOINT_URL'),
            data=json.dumps(notification),
            headers={
                'Authorization': 'key='+config.get('API', 'FIREBASE_NOTIFICATION_ENDPOINT_KEY'),
                'Content-Type': 'application/json'
            }
        )

        return response
