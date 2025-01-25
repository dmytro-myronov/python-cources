class Singleton:
    """
    Implements the Singleton design pattern.

    This class ensures that only one instance of the class exists at any given
    time. It provides a global point of access to the single instance and
    controls its creation. If the instance already exists, it returns the
    existing one; otherwise, it creates a new instance.

    :ivar instance: Holds the single instance of the class.
    :type instance: object
    """
    instance = None

    def __new__(cls):
        """
        Represents the instantiation process for a class object. This is
        used to control and define the behavior when a new instance of
        the class is created. The method allows customization of object
        creation prior to the initialization phase of the instance.

        :param cls: The class being instantiated. This parameter is
            implicitly passed to the method when creating an object.
        :type cls: type

        :returns: A new instance of the given class.
        :rtype: object
        """
        pass

    def __init__(self):
        pass

    def get_instance(self)-> object:
        """
        Provides a method to retrieve the singleton instance of the `Singleton` class.
        Ensures that only one instance of the `Singleton` class is created throughout
        the lifetime of the application. The instance is either created or the existing
        one is returned.

        :return: A singleton instance of the `Singleton` class.
        :rtype: object
        """
        if Singleton.instance is None:
            return Singleton()
        else:
            return Singleton.instance


single1 = Singleton()
single2 = Singleton()
print(single1 is single2)