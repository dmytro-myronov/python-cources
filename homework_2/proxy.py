class Some:
    """
    A simple class with two methods: method_one and method_two.

    Methods:
        method_one(name): Prints a greeting message with the provided name.
        method_two(): Prints a generic greeting message.
    """
    def method_one(self, name):
        """
        Prints a greeting message with the provided name.

        Args:
            name (str): The name to include in the greeting message.
        """
        print(f"hi 1 : {name}")

    def method_two(self):
        """Prints a generic greeting message."""
        print("hi 2")


class ProxySome(Some):
    """
    A proxy class that wraps an instance of the Some class and adds additional behavior to method calls.

    Args:
        obj_to_proxy (Some): An instance of the Some class to be proxied.

    Methods:
        method_one(name): Logs a message before calling method_one of the proxied object.
    """
    def __init__(self, obj_to_proxy):
        """
        Initializes the ProxySome instance with an object to proxy.

        Args:
            obj_to_proxy (Some): The object to proxy.
        """
        self.obj = obj_to_proxy

    def method_one(self, name):
        """
        Logs a message and delegates the call to the proxied object's method_one.

        Args:
            name (str): The name to pass to the proxied method_one.
        """
        print("login something")
        self.obj.method_one(name)


# Example usage:
obj = Some()
proxy = ProxySome(obj)
proxy.method_one('Alice')  # Output will include "login something" followed by "hi 1 : Alice"
