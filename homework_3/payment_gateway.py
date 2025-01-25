class PriceWithGetSet:
    """
    Provides a structure to store, retrieve, and set a price value.

    This class is designed to encapsulate a price value and provide getter and
    setter methods for safe access and modification of the price attribute. It
    is useful in scenarios where controlled access to the price value is
    required.

    :ivar price: The monetary value representing the price.
    :type price: float
    """
    def __init__(self, price: float):
        self.price = price

    def set_price(self, price: float) -> None:
        """
        Updates the price attribute of the object to the specified value.

        This method allows setting a new value for the price attribute,
        ensuring that the object reflects the latest pricing data.

        :param price: The new price value to assign.
        :type price: float
        :return: None
        :rtype: None
        """
        self.price = price

    def get_price(self) -> float:
        """
        Returns the price of the item.

        This method retrieves the price attribute of the object, which represents
        the cost of the item. The value is expected to be a floating-point number.

        :return: The price of the item.
        :rtype: float
        """
        return self.price


class PaymentGatewayInterface:
    """
    Interface for implementing payment gateway functionalities.

    This class serves as a blueprint for various payment gateway
    implementations. It defines the required methods for processing
    payments and ensures consistency across different implementations.

    :ivar pay: Process the payment with the given price object.
    :type pay: method
    """
    def pay(self, price_obj: PriceWithGetSet):
        pass


class PaymentGateway(PaymentGatewayInterface):
    """
    Represents a payment gateway interface that facilitates processing
    of payments.

    Provides functionality to process a payment for a given price object
    that encapsulates price value. This payment gateway enforces validation
    on the provided price to ensure it conforms to acceptable value
    constraints.

    """
    def pay(self, price_obj: PriceWithGetSet):
        price_value = price_obj.get_price()
        if price_value <= 0:
            raise ValueError('Price must be gr then zero')
        print(f'Paying {price_value}')


price_element = PriceWithGetSet(10)
price_element.set_price(100)
payment_gateway = PaymentGateway()
payment_gateway.pay(price_element)
