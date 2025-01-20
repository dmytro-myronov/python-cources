class MutableClass:
    """
    A class that allows dynamic addition and removal of attributes.
    """

    def add_attribute(self, name: str, value: any):
        """
        Adds an attribute to the object dynamically.

        Args:
            name (str): The name of the attribute to add.
            value (any): The value to assign to the attribute.
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str):
        """
        Removes an attribute from the object if it exists.

        Args:
            name (str): The name of the attribute to remove.
        """
        if hasattr(self, name):
            delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # This will raise an AttributeError since the attribute is removed
