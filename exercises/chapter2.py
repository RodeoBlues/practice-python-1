class Flower:
    """this class has three instance variables of type str, int,
    and float, that respectively the name of the flower,
    its number of petals, and its price."""

    def __init__(self, name='Rose', petals_number=0, price=1):
        self._name = name
        self._petals_number = petals_number
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_petals_number(self, number):
        self._petals_number = number

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_petals_number(self):
        return self._petals_number

    def get_price(self):
        return self._price

flower = Flower()

