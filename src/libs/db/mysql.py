import mysql.connector
from src import config
from src.libs.db import map_data_with_columns
from src.libs.db.db import DB
from datetime import datetime


class MySQL(DB):
    def __init__(self):
        super().__init__()
        self.db = mysql.connector.connect(
            host=config.get('MySQL', 'HOST'),
            port=config.getint('MySQL', 'PORT'),
            user=config.get('MySQL', 'USER'),
            password=config.get('MySQL', 'PASSWORD'),
            database=config.get('MySQL', 'DATABASE'),
        )
        self.cursor = self.db.cursor()

    def get_currency(self):
        self.cursor.execute('SELECT * FROM `currency` ORDER BY `id`;')

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_exchange_rates(self, requested_date: str = None):
        date_query = ''
        if requested_date is not None:
            date_query = 'WHERE `date` = "{}"'.format(requested_date)

        self.cursor.execute('SELECT * FROM `exchange_rates` {};'.format(date_query))

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_rates_by_date_range(self, date_from: str, date_to: str):
        pass

    def save_exchange_rates(self, exchange_rates: list, requested_date: str):
        insert_values, existing_currency = self.prepare_insert_values(exchange_rates, requested_date)

        if insert_values:
            query = 'INSERT INTO `exchange_rates` (`currency_id`, `value`, `date`) ' \
                    'VALUES {} ' \
                    'ON DUPLICATE KEY UPDATE `value`=VALUES(`value`);'

            self.cursor.execute(query.format(','.join(insert_values)))
            self.db.commit()
            return {'message': 'Save rates for {} currencies ({})'.format(
                ', '.join(existing_currency),
                datetime.strptime(requested_date, '%Y%m%d').strftime('%d.%m.%Y')
            )}

        return {'message': 'No values to save'}

    def prepare_insert_values(self, exchange_rates: list, requested_date: str):
        existing_currency = []
        existing_currency_ids = {}

        for currency in self.get_currency():
            existing_currency.append(currency['code'])
            existing_currency_ids[currency['code']] = currency['id']

        values = []
        for rate in exchange_rates:
            if rate['cc'] in existing_currency:
                values.append('({}, {}, {})'.format(
                    existing_currency_ids[rate['cc']],
                    rate['rate'],
                    requested_date
                ))

        return values, existing_currency

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
