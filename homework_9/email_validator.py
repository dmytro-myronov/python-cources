import re

def validate_email(email: str) -> bool:
    """
    Validates an email address to ensure it matches a specific pattern.

    The pattern ensures:
    - The email does not start with a dot.
    - Allowed characters before the '@' include letters, digits, dots, underscores, percent, plus, and hyphens.
    - The domain contains letters, digits, dots, and hyphens.
    - The top-level domain is one of: .com, .net, or .org.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid according to the pattern, False otherwise.
    """
    val = re.match(r'^[^\.][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|net|org)$', email)
    return bool(val)


# Example usage
is_valid = validate_email('a@dom.com')
print(is_valid)

is_valid2 = validate_email('afer@gmail.com')
print(is_valid2)
