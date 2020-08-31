from flask import Flask, session, request
from src.libs import MySQL, Response
from src.services import CurrenciesClient
from src import __version__
from time import time

app = Flask(__name__)

app.secret_key = '5cb89b235901119c679e09dda78470e6'


@app.route('/api/v{}/save_currencies'.format(__version__))
def save_currencies():
    requested_date = request.args.get('date')
    currencies = CurrenciesClient().get_currencies_by_date(requested_date)

    return Response(MySQL().save_currencies(currencies, requested_date)).json()


@app.route('/api/v{}/currencies'.format(__version__))
def get_currencies():
    currencies = MySQL().get_currencies()

    return Response(currencies).json()


@app.route('/api/v{}/currency_rates'.format(__version__))
def get_currency_rates():
    currency_rates = MySQL().get_currency_rates()

    return Response(currency_rates).json()


@app.errorhandler(Response.codes['NOT_FOUND'])
def page_not_found(e):
    return Response.not_found()


@app.errorhandler(Exception)
def handle_exception(e):
    return Response.internal_server_error(e)


@app.before_request
def before_request():
    session['start_time'] = time()


if __name__ == '__main__':
    app.run()
