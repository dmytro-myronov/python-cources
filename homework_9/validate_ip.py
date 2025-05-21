import re

def is_ip(ip: str) -> bool:
    """
    Validates whether a given string is a valid IPv4 address.

    A valid IPv4 address:
    - Has four octets separated by dots.
    - Each octet is a number from 0 to 255 (inclusive).
    - Must not contain any non-numeric or extra characters.

    Args:
        ip (str): The input string to validate as an IP address.

    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """
    if re.fullmatch(r'\d{1,3}(\.\d{1,3}){3}', ip):
        ip_parts = ip.split('.')
        for part in ip_parts:
            try:
                value = int(part)
                if not (0 <= value <= 255):
                    return False
            except ValueError:
                return False
        return True
    return False


# Example usage
is_valid_ip = is_ip('150.168.10.1')         # True
is_valid_ip2 = is_ip('_150.168.10.1')       # False
print(is_valid_ip)
print(is_valid_ip2)
