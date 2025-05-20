import re


def is_strong_password(password)->bool:
    # Мінімум 8 символів
    if len(password) < 8:
        return False

    # Хоча б одна цифра
    if not re.search(r'\d', password):
        return False

    # Хоча б одна велика літера
    if not re.search(r'[A-Z]', password):
        return False

    # Хоча б одна мала літера
    if not re.search(r'[a-z]', password):
        return False

    # Хоча б один спеціальний символ
    if not re.search(r'[@#$%&*!?]', password):
        return False

    return True

print(is_strong_password("Abc123$"))        # False — менше 8 символів
print(is_strong_password("Abcdefgh"))       # False — немає цифри і спецсимволу
print(is_strong_password("Abc12345"))       # False — немає спецсимволу
print(is_strong_password("Abc123$%"))