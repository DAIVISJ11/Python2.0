import math

class Circle:
    def __init__(self, radius):
        """Initialise the circle with a radius."""
        self.radius = radius

    def calculate_area(self):
        """Calculate and return the area using πr²."""
        return math.pi * (self.radius ** 2)


user_radius = float(input("Enter the radius of the circle: "))


my_circle = Circle(user_radius)


area = my_circle.calculate_area()

print(f"The area of a circle with radius {user_radius} is: {area:.2f}")
