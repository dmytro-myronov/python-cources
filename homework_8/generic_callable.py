

class Processor:
    def __init__(self, data):
        self.data = data

    def apply(self, callable):
        return list(map(callable, self.data))


p1 = Processor([1, 2, 3])
print(p1.apply(lambda x: x * 2))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(str.upper))  # ["HELLO", "WORLD"]
