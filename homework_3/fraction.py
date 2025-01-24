class Number:
    def __init__(self, number: float):
        self.number = number

    def __add__(self, new_num: float):
        if isinstance(new_num, Number):
            return float(self.number) + new_num.number
        elif isinstance(new_num, float) or isinstance(new_num, int):
            return self.number + float(new_num)
        return NotImplemented

    def __sub__(self, new_num: float):
        if isinstance(new_num, Number):
            return float(self.number) - new_num.number
        elif isinstance(new_num, float) or isinstance(new_num, int):
            return self.number - float(new_num)
        return NotImplemented

    def __mul__(self, new_num):
        if isinstance(new_num, Number):
            return float(self.number) * new_num.number
        elif isinstance(new_num, float) or isinstance(new_num, int):
            return self.number * float(new_num)
        return NotImplemented

    def __truediv__(self, new_num):
        if isinstance(new_num, Number):
            return float(self.number) / new_num.number
        elif isinstance(new_num, float) or isinstance(new_num, int):
            return self.number / float(new_num)
        return NotImplemented

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.number


number1 = Number(16.00)
number2 = Number(8.00)

print(number1 + 5)
print("----")
print(number1 + number2)
print("----substraction")
print(number1 - number2)
print("----")
print(number1 - 5.00)
print("----multiply")
print(number1 * number2)
print("----")
print(number1 * 5)
print("----division")

print(number1 / number2)
print("----")
print(number1 / 2)
print("----number1")
print(number1)
print("----number2")
print(number2)
