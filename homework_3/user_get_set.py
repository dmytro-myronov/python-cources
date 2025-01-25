import re


class User:
    """
    A class representing a user with attributes for first name, last name, and email.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
    """

    def __init__(self, first_name, last_name, email):
        """
        Initializes a new User instance.

        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.

        Raises:
            ValueError: If the first name, last name, or email is invalid.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        """Gets the user's first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the user's first name.

        Args:
            value (str): The first name to set.

        Raises:
            ValueError: If the first name contains non-alphabetic characters.
        """
        if not value.isalpha():
            raise ValueError("First name must contain only letters.")
        self._first_name = value

    @property
    def last_name(self):
        """Gets the user's last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the user's last name.

        Args:
            value (str): The last name to set.

        Raises:
            ValueError: If the last name contains non-alphabetic characters.
        """
        if not value.isalpha():
            raise ValueError("Last name must contain only letters.")
        self._last_name = value

    @property
    def email(self):
        """Gets the user's email address."""
        return self._email

    @email.setter
    def email(self, value):
        """
        Sets the user's email address.

        Args:
            value (str): The email address to set.

        Raises:
            ValueError: If the email format is invalid.
        """
        if not self.is_valid_email(value):
            raise ValueError("Invalid email format.")
        self._email = value

    @staticmethod
    def is_valid_email(email):
        """
        Validates the format of an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

try:
    user = User("Dima", "Myronov", "dima@gmail.com")
    print(user.first_name)
    print(user.last_name)
    print(user.email)

    user.email = "invalid_email"  # Will raise ValueError
except ValueError as e:
    print(e)
