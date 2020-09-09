from abc import ABC, abstractmethod


class DB(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_currency(self):
        pass

    @abstractmethod
    def get_exchange_rates(self, requested_date: str = None):
        pass

    @abstractmethod
    def get_rates_by_date_range(self, date_from: str, date_to: str):
        pass
