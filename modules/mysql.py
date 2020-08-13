import mysql.connector


class MySQL:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            port=3309,
            user="root",
            password="",
            database="test"
        )

    def get_currencies(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM currencies")

        return cursor.fetchall()

    def get_currency_rates(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM currency_rates")

        return cursor.fetchall()

    def get_last_five_days_currencies(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT c.code, cr.value, cr.date \
                        FROM currency_rates cr \
                        LEFT JOIN currencies c ON c.id = cr.currency_id \
                        ORDER BY cr.date")

        return cursor.fetchall()
