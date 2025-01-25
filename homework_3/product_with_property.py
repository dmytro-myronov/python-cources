
class PriceWithProperty:
    """
    Represents a price management system with getter and setter functionality.

    This class enables encapsulation of the price attribute and provides validation
    through the setter to ensure that only values greater than zero are accepted.

    :ivar _price: Encapsulated attribute representing the price.
    :type _price: float
    """
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Price must be gr then zero')
        self._price = value


price_el = PriceWithProperty(10)
p = price_el.price
price_el.price = 100
print(price_el.price)