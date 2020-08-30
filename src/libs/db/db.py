from abc import ABC, abstractmethod


class DB(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_currencies(self):
        pass

    @abstractmethod
    def get_currency_rates(self):
        pass

    @abstractmethod
    def get_rates_by_date_range(self, date_from: str, date_to: str):
        pass
