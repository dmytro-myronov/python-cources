
def analyze_object(obj: object) -> None:
    """
    Analyze an object to display its type, class name, methods, and parameters.

    :param obj: The object to analyze.
    """
    class_name = obj.__class__.__name__
    print(type(obj))
    print(f"Class: {class_name}")
    print(dir(obj))
    print("Methods:", [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith("__")])
    print("Params:", [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")])


class MyClass:
    """
    A simple class to demonstrate object analysis.

    Attributes:
        name (str): A string value associated with the instance.
        email (str): An email address associated with the instance.
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a MyClass instance.

        :param name: A string value to initialize the instance with.
        :param email: An email address to associate with the instance.
        """
        self.name = name
        self.email = email

    def say_hello(self) -> str:
        """
        Return a greeting message.

        :return: A greeting string including the instance's value.
        """
        return f"Hello, {self.name}"

    def get_email(self) -> str:
        """
        Get the email address associated with the instance.

        :return: The email address as a string.
        """
        return self.email


# Create an instance of MyClass
my_class_obj = MyClass("Dima", "dima@gmail.com")

# Analyze the object
analyze_object(my_class_obj)
