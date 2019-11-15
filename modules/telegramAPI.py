import requests

telegramAPIUrl = "https://api.telegram.org/bot657973439:AAHDoDXQaVj4aLe1-ZCnvqlv2_EGWnu1rGU/sendMessage?chat_id=-1001494891755&text="


def sendMessage(message):
    return requests.get(telegramAPIUrl + message).content
