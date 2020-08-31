import sys, inspect, configparser
from os.path import dirname, abspath
current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
parent_dir = dirname(current_dir)

# add parent dir ("/src") to import folders
sys.path.insert(0, parent_dir)

from src.libs import MySQL
from src.services import CurrenciesClient
from datetime import date


config = configparser.ConfigParser()
config.read('settings.ini')

MySQL().save_currencies(
    CurrenciesClient().get_currencies_by_date(),
    date.today().strftime("%Y%m%d")
)
