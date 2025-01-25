

class PriceCurrencyDescriptor:
    def __set__(self, instance, currency):
        if currency not in ('USD', 'EUR'):
            raise ValueError('Currency must be USD or EUR')
        instance.__dict__['currency'] = currency

class PriceDescriptor:
    """
    Descriptor class for controlling the `price` attribute. Provides a mechanism to validate and manage
    the `price` attribute in the class where it is used. The getter method retrieves the price value,
    and the setter method enforces a constraint that the price must be greater than zero.

    This class is designed to be used as a descriptor for encapsulating and validating data.

    Methods:
        __get__: Retrieves the value of the 'price' attribute.
        __set__: Validates and sets the value of the 'price' attribute in an instance.
    """
    def __get__(self, instance, owner):
        return instance.__dict__.get('price')

    def __set__(self, instance, price):
        if price <= 0:
            raise ValueError('Price must be gr then zero')
        instance.__dict__['price'] = price

class PriceWithDescriptor:

    """
    Represents a class that uses descriptors to manage pricing values.

    This class demonstrates the usage of a descriptor for managing the
    price attribute. It provides methods for setting and getting the
    price value through the descriptor. The purpose of the class is to
    encapsulate pricing-related functionality while leveraging Python's
    descriptor protocol for advanced attribute manipulation.

    :ivar price: Represents the price value which is handled by the
        PriceDescriptor.
    :type price: PriceDescriptor
    """
    price = PriceDescriptor()
    currency = PriceCurrencyDescriptor()
    def __init__(self, price: float, currency='USD') -> None:
        self._price = price
        self.currency = currency

    def set_price(self, price: float, currency='USD')-> None:
        """

        :param currency:
        :type price: float
        """
        self.price = price
        self.currency = currency

    def get_price(self):
        return self.price


    def get_currency(self):
        return self.currency

class PriceCurrencyConverter:
    MAIN_CURRENCY = 'USD'
    CURRENCY_MAPPER = dict(EUR=0.91, USD=1.00)

    def convert(self, price: PriceWithDescriptor, currency: str):

        if price.currency == currency:
            return price.price
        else:
            try :
                value_currency = self.CURRENCY_MAPPER[currency]
                return price.price * value_currency
            except KeyError as e:
                print("please provide valid currency")


converter = PriceCurrencyConverter()

price_el = PriceWithDescriptor(10.00)
price_el.set_price(20)
pr_el = price_el.get_price()
currency_el = price_el.get_currency()

print(f"price: {pr_el} currency: {currency_el}")
print("convert")
print("price {},currency:{}".format(converter.convert(price_el, 'EUR') ,'EUR'))