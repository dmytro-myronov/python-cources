def say_hello(self):
    """
    Returns a greeting message.

    :return: A string "Hello!"
    """
    return "Hello!"


def say_goodbye(self):
    """
    Returns a farewell message.

    :return: A string "Goodbye!"
    """
    return "Goodbye!"


# Dictionary containing methods for the dynamic class
methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}


def create_class(class_name: str, methods: dict):
    """
    Dynamically creates a class with the given name and methods.

    :param class_name: The name of the class to be created.
    :param methods: A dictionary of method names and their corresponding function implementations.
    :return: A new class with the specified methods.
    """
    return type(class_name, (object,), methods)


# Create the dynamic class
MyDynamicClass = create_class("MyDynamicClass", methods)

# Create an instance of the dynamically created class
obj = MyDynamicClass()

# Call the methods
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
