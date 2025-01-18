class Rectangle:
    """
    A class to represent a rectangle and perform operations related to it.
    """

    def __init__(self, rect_width: float, rect_height: float):
        """
        Initializes a new Rectangle object with width and height.

        Args:
            rect_width (float): The width of the rectangle.
            rect_height (float): The height of the rectangle.
        """
        self.width: float = rect_width
        self.height: float = rect_height

    def calculate_area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square (i.e., width equals height).

        Returns:
            bool: True if the rectangle is a square, False otherwise.
        """
        return self.width == self.height

    def resize(self, res_width: float, res_height: float) -> None:
        """
        Resizes the rectangle to a new width and height.

        Args:
            res_width (float): The new width of the rectangle.
            res_height (float): The new height of the rectangle.
        """
        self.width = res_width
        self.height = res_height


# Main program loop
end: bool = False  # Type hint for the end variable
while not end:
    try:
        width_input: str = input("Please enter width of rectangle (write `end` to stop program): ")
        height_input: str = input("Please enter height of rectangle (write `end` to stop program): ")

        if width_input.lower() == "end" or height_input.lower() == "end":
            end = True
            print('Exiting the program!')
            break

        width: float = float(width_input)  # Type hint for width
        height: float = float(height_input)  # Type hint for height

        if width > 0 and height > 0:
            rect = Rectangle(width, height)
            print(f"Rectangle area: {rect.calculate_area()}")
            print(f"Rectangle perimeter: {rect.calculate_perimeter()}")
            print("Rectangle is square:" if rect.is_square() else "Rectangle is not square.")
        else:
            print("Numbers must be greater than zero!")

    except ValueError:
        print('Please provide valid numbers for width and height!')
