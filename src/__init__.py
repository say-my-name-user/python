import configparser


config = configparser.ConfigParser()
config.read('settings.ini')

__version__ = '1.0'
