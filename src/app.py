from flask import Flask, session, request
from src.libs import MySQL, Response
from src.services import ExchangeRatesClient
from src import __version__
from time import time

app = Flask(__name__)

app.secret_key = '5cb89b235901119c679e09dda78470e6'


@app.route('/api/v{}/save_exchange_rates'.format(__version__))
def save_exchange_rates():
    currency_list, requested_date = ExchangeRatesClient().get_rates_by_date(request.args.get('date'))

    return Response(MySQL().save_exchange_rates(currency_list, requested_date)).json()


@app.route('/api/v{}/currency'.format(__version__))
def get_currency():
    currencies = MySQL().get_currency()

    return Response(currencies).json()


@app.route('/api/v{}/exchange_rates'.format(__version__))
def get_exchange_rates():
    currency_rates = MySQL().get_exchange_rates(request.args.get('date'))

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


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run()
