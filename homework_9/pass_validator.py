import re

def is_strong_password(password: str) -> bool:
    """
    Checks whether a password is strong based on the following criteria:
    - At least 8 characters long
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character from [@#$%&*!?]

    Args:
        password (str): The password string to validate.

    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[@#$%&*!?]', password):
        return False

    return True


# Example usage
print(is_strong_password("Abc123$"))        # False — менше 8 символів
print(is_strong_password("Abcdefgh"))       # False — немає цифри і спецсимволу
print(is_strong_password("Abc12345"))       # False — немає спецсимволу
print(is_strong_password("Abc123$%"))       # True
