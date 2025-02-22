from typing import Union


def parse_input(input_string: Union[int, str]) -> Union[int, None]:
    if isinstance(input_string, str):
        try:
            int_value = int(input_string)
            return int_value
        except ValueError:
            return  None

    elif isinstance(input_string, int):
        return input_string
    else:
        return None




print(parse_input(42))       # 42
print(parse_input("100"))    # 100
print(parse_input("hello"))  # None
print(parse_input(2.3))  # None