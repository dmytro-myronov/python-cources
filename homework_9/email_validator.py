import re

def validate_email(email):
    val = re.match( r'^[^\.][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|net|org)$', email)
    return bool(val)
    # if '@' not in email:
    #     return False
    #
    # return True


is_valid = validate_email('a@dom.com')
print(is_valid)
is_valid2= validate_email('afer@gmail.com')
print(is_valid2)


#[A-Za-z0-9]+
#^[A-Za-z0-9]{7,} - отрицание
# [\W]{7,} - спецсиф все кроме букв
# [\w]{7,} - любой символ
# [\d]{,3} - любые числа
# \s  - пробел
# \b - початок
# \B - Не початок
# \S - все кроме пробела
# + от 1 и больше пробелов
# * -квантификатор - повторение 0 и более раз