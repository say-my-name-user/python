from urllib.request import urlopen
import json

APIUrl = "http://api.openweathermap.org/data/2.5/weather?id={cityId}&APPID=62185ad02a7052006dcc36bb2ed527eb"


def getForecast(cityId = 686967):
    return json.loads(urlopen(APIUrl.replace("{cityId}", str(cityId))).read())
