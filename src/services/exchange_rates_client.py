import requests
import json
from src import config
from datetime import date


class ExchangeRatesClient:
    @staticmethod
    def get_rates_by_date(requested_date: str = None):
        """requested_date parameter must be in YYYYMMDD format"""

        if requested_date is None:
            requested_date = date.today().strftime("%Y%m%d")

        response = requests.get(url=config.get('API', 'EXCHANGE_RATES_ENDPOINT').format(requested_date))

        return json.loads(response.content), requested_date
