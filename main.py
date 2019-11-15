import pymongo
import datetime
from modules.weatherAPI import getForecast
from notify_run import Notify

try:
    forecast = getForecast()

    # 1. save forecast to db
    mongo = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo["weather"]
    collection = db[forecast["name"]]

    forecast["_id"] = forecast["dt"]
    collection.update_one(forecast, {'$set': forecast}, True)

    # 2. send push notification about current weather
    message = "Hi,today is {},clouds:{}%,\n" \
              "t°:{}°C,wind:{}m/s,{}mmHg,humidity:{}%.\n" \
              "Sun will set at {}. Have a nice day! :) "

    Notify().send(message.format(
        forecast["weather"][0]["description"],
        forecast["clouds"]["all"],
        round(forecast["main"]["temp"] - 273.15),
        forecast["wind"]["speed"],
        round(forecast["main"]["pressure"] / 1.33322),
        forecast["main"]["humidity"],
        datetime.datetime.fromtimestamp(forecast["sys"]["sunset"]).strftime("%H:%M"),
    ))
except:
    print("Something went wrong.")
