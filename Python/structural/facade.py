class BanknoteProcessor:
    DENOMINATIONS = (1, 5, 10, 20, 50, 100)

    def __init__(self, bills, price):
        self.bills = bills
        self.price = price

    def validate_entered_bills(self):
        return (all(bill in self.DENOMINATIONS for bill in self.bills) and
                self._is_amount_enough())

    def _is_amount_enough(self):
        return sum(self.bills) >= self.price


class ItemRegistry:
    items = [
        {
            'name': 'Coca-Cola',
            'price': 6,
            'coordinates': 'A1'
        },
        {
            'name': 'Pepsi',
            'price': 5,
            'coordinates': 'A2'
        }
    ]

    def get_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                return item


class MechanismController:
    def deliver_item(self, coordinates):
        print(f'Moving the mechanism to deliver item at {coordinates}...')


class VendingMachine:
    """
    Facade
    """
    def __init__(self):
        self.item_registry = ItemRegistry()
        self.controller = MechanismController()

    def new_sale(self, item_name, bills):
        item = self.item_registry.get_item(item_name)
        valid_input = (BanknoteProcessor(bills, item['price'])
                       .validate_entered_bills())
        if valid_input:
            self.controller.deliver_item(item['coordinates'])
        else:
            print("The machine couldn't deliver the requested item")


class User:
    """
    Client
    """
    def __init__(self):
        self.bills = [5]

    def buy(self, item_name):
        vending_machine = VendingMachine()
        vending_machine.new_sale(item_name, self.bills)


user = User()
user.buy('Coca-Cola')
user.buy('Pepsi')
