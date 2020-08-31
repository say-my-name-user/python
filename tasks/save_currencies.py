import sys, configparser
from os.path import dirname, abspath, join
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)

# add parent dir ("/src") to import folders
sys.path.insert(0, parent_dir)

from src.libs import MySQL
from src.services import CurrenciesClient
from datetime import date


config = configparser.ConfigParser()
config.read(join(parent_dir, 'settings.ini'))

try:
    currencies = CurrenciesClient().get_currencies_by_date()
except Exception:
    currencies = CurrenciesClient().get_currencies_by_date()

MySQL().save_currencies(
    currencies,
    date.today().strftime("%Y%m%d")
)
