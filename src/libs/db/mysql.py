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

    def get_currencies(self):
        self.cursor.execute("SELECT * FROM `currencies`;")

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_currency_rates(self):
        self.cursor.execute("SELECT * FROM `currency_rates`;")

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_rates_by_date_range(self, date_from: str, date_to: str):
        pass

    def save_currencies(self, currencies: list, requested_date: str):
        insert_values, existing_currencies = self.prepare_insert_values(currencies, requested_date)

        if insert_values:
            query = "INSERT INTO `currency_rates` (`currency_id`, `value`, `date`) " \
                    "VALUES {} " \
                    "ON DUPLICATE KEY UPDATE `value`=VALUES(`value`);"

            self.cursor.execute(query.format(','.join(insert_values)))
            self.db.commit()
            return {'message': 'Save rates for {} currencies ({})'.format(
                ', '.join(existing_currencies),
                datetime.strptime(requested_date, '%Y%m%d').strftime('%d.%m.%Y')
            )}

        return {'message': 'No values to save'}

    def prepare_insert_values(self, currencies: list, requested_date: str):
        existing_currencies = []
        existing_currency_ids = {}

        for existing_currency in self.get_currencies():
            existing_currencies.append(existing_currency['code'])
            existing_currency_ids[existing_currency['code']] = existing_currency['id']

        values = []
        for currency in currencies:
            if currency['cc'] in existing_currencies:
                values.append('({}, {}, {})'.format(
                    existing_currency_ids[currency['cc']],
                    currency['rate'],
                    requested_date
                ))

        return values, existing_currencies

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
