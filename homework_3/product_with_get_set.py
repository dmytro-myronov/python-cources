class PriceWithGetSet:
    """
    Represents an object that encapsulates a price value with getter and setter
    methods for controlled access and modification.

    This class is intended for managing a price value, allowing external
    components to safely retrieve or update this value using dedicated methods.

    :ivar price: The monetary value associated with the object.
    :type price: float
    """
    def __init__(self, price: float):
        self.price = price

    def set_price(self, price: float):
        """
        Sets the price of an item.

        This method assigns a specified price to an item. It takes a float as the
        price value and updates the corresponding attribute to the provided value.

        :param price: The price value to set for the item.
        :type price: float
        """
        self.price = price

    def get_price(self) -> float:
        """
        Retrieves the price of the object.

        This method is used to access the `price` attribute of the object. It provides
        a float value that represents the price.

        :return: The price of the object.
        :rtype: float
        """
        return self.price


price_el = PriceWithGetSet(10.00)
price_el.set_price(20.00)
pr_el = price_el.get_price()
print(pr_el)