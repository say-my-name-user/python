import requests


class CurrencyClient:
    def __init__(self):
        self.endpoint = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20200813"

    def get_today_currencies(self):
        r = requests.get(url=self.endpoint)

        # TODO: parse xml
        print(r.content)
