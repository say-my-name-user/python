import requests
import json
from src import config
from datetime import date


class CurrenciesClient:
    @staticmethod
    def get_currencies_by_date(requested_date: str = None):
        if requested_date is None:
            requested_date = date.today().strftime("%Y%m%d")

        response = requests.get(url=config.get('API', 'CURRENCIES_ENDPOINT').format(requested_date))

        return response.content  # TODO: json.loads(response.content)
