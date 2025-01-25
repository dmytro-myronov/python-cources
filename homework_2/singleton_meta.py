class SingletonMeta(type):
    """
    A metaclass for implementing the Singleton design pattern.

    This ensures that only one instance of a class is created.
    Subsequent attempts to create an instance will return the same object.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override the default behavior of creating an instance.
        If an instance of the class already exists, return it.
        Otherwise, create a new instance and store it in the `_instances` dictionary.
        """
        if cls not in cls._instances:
            # Create a new instance and store it
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    """
    Example class using the SingletonMeta metaclass.
    """

    def __init__(self, value):
        """
        Initialize the singleton instance with a value.
        """
        self.value = value

class SingletonClass2(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name



# Usage example
singleton1 = SingletonClass("First Instance")
singleton2 = SingletonClass("Second Instance")

singleton3 = SingletonClass2("instance singleton class2")

# Verify that both variables point to the same instance
print(singleton1 is singleton2)  # True
print(singleton1.value)          # "First Instance"
print(singleton2.value)          # "First Instance"
