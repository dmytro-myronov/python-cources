class Rectangle:

    def __init__(self, rect_width, rect_height):
        self.width = rect_width
        self.height = rect_height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimetr(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, res_width, res_height):
        self.width = res_width
        self.height = res_height


end = False
while end is False:

    try:
        width = input("please enter width of rectangle(write `end` to stop program): ")
        height = input("please enter height of rectangle(write `end` to stop program): ")

        if width == "end" or height == "end":
            end = True
            print('exit from program!')
            break
        width = float(width)
        height = float(height)
        if width > 0 and height > 0:
            rect = Rectangle(width, height)
            print("rectangle area: " + str(rect.calculate_area()))
            print("rectangle perimetr: " + str(rect.calculate_perimetr()))
            print("rectangle is square:" if rect.is_square() else "rectangle is not square:")
        else:
            print("numbers must be great then zero!")
    except ValueError as e:
        print('Please provide correct number!')
