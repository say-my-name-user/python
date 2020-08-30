import mysql.connector
from src import config
from src.libs.db import map_data_with_columns
from src.libs.db.db import DB


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
        self.cursor.execute("SELECT * FROM currencies;")

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_currency_rates(self):
        self.cursor.execute("SELECT * FROM currency_rates;")

        return map_data_with_columns(self.cursor.fetchall(), self.cursor.column_names)

    def get_rates_by_date_range(self, date_from: str, date_to: str):
        pass

    def save_currencies(self, currencies):
        # TODO: implement method
        pass

    def __del__(self):
        self.cursor.close()
