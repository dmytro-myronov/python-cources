import math


class CalculateCircle:

    def calculate_circle(self, circle_radius):
        return math.pi * circle_radius ** 2


end = False
while end is False:
    try:
        radius = input("Please provide radius to calculate circle area(or write end to stop and exit program): ")
        if radius == "end":
            end = True
            print('exit from program!')
            break
        radius = float(radius)
        if radius > 0:
            calculateCircle = CalculateCircle()
            area = calculateCircle.calculate_circle(radius)
            print(area)

    except ValueError as e:
        print('Please provide correct number!')
