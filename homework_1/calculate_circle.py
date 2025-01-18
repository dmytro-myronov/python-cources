import math


class CalculateCircle:
    """
    A class to perform calculations related to circles.
    """

    def calculate_circle(self, circle_radius: float) -> float:
        """
        Calculates the area of a circle given its radius.

        Args:
            circle_radius (float): The radius of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * circle_radius ** 2


# Main program loop
end: bool = False  # Type hint for the end variable
while not end:
    try:
        radius_input: str = input("Please provide radius to calculate circle area (or write 'end' to stop and exit "
                                  "program): ")
        if radius_input.lower() == "end":
            end = True
            print('Exiting the program!')
            break
        radius: float = float(radius_input)  # Type hint for radius
        if radius > 0:
            calculateCircle = CalculateCircle()
            area: float = calculateCircle.calculate_circle(radius)  # Type hint for area
            print(f"Circle area: {area}")
        else:
            print("Radius must be greater than zero.")

    except ValueError:
        print('Please provide a valid number for the radius!')
