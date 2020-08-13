from flask import Flask
from modules import Response, MySQL, Transformer, CurrencyClient

app = Flask(__name__)


@app.route('/currencies')
def get_currencies():
    currencies = MySQL().get_currencies()

    # TODO
    # CurrencyClient().get_today_currencies()

    return Response(currencies).encode()


@app.route('/currency_rates')
def get_currency_rates():
    currency_rates = MySQL().get_currency_rates()

    return Response(currency_rates).encode()


@app.route('/last_five_days_currencies')
def get_last_five_days_currencies():
    currency_rates = MySQL().get_last_five_days_currencies()
    currency_rates = Transformer(currency_rates).prepare_currency_response()

    return Response(currency_rates).encode()


@app.errorhandler(404)
def page_not_found(e):
    return Response().not_found(), 404


@app.errorhandler(Exception)
def handle_exception(e):
    return Response().internal_server_error(e), 500


if __name__ == '__main__':
    app.run()

__version__ = '1.0'
