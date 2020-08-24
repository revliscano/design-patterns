from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Strategy interface
    """

    @abstractmethod
    def get_meal(self):
        pass


class VeganMeal(Strategy):
    """
    Concrete strategy
    """
    def get_meal(self):
        print('Preparing Gazpacho')


class Barbeque(Strategy):
    """
    Concrete strategy
    """
    def get_meal(self):
        print('Preparing Spareribs')


class Chef:
    """
    Context
    """
    def set_strategy(self, strategy):
        self.strategy = strategy()

    def prepare_meal(self):
        return self.strategy.get_meal()


class Restaurant:
    def __init__(self, chef):
        self.chef = chef

    def take_order(self, client):
        if client.is_vegan():
            self.chef.set_strategy(VeganMeal)
        else:
            self.chef.set_strategy(Barbeque)

    def dispatch_order(self):
        self.chef.prepare_meal()
        print('Order dispatched')


class Client:
    def __init__(self, veganism=False):
        self.veganism = veganism

    def is_vegan(self):
        return self.veganism


restaurant = Restaurant(Chef())
vegan_client = Client(veganism=True)
client = Client()
restaurant.take_order(vegan_client)
restaurant.dispatch_order()
restaurant.take_order(client)
restaurant.dispatch_order()
