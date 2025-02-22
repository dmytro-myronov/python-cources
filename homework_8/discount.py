def calculate_discount(price, discount):
    if discount > 100:
        return 0
    return price - (price * discount / 100)


price = 120
discount = 10
print(calculate_discount(price, discount))