import math

# Base class for Polygon
class Polygon:
    def __init__(self):
        # Encapsulation: Private attribute for storing the name
        self._name = "Polygon"

    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

    def get_name(self):
        # Getter method to access the name
        return self._name

# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__()
        # Encapsulation: Private attributes for width and height
        self.__width = width
        self.__height = height
        self._name = "Rectangle"

    def area(self):
        # Overriding the base class method
        return self.__width * self.__height

# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__()
        # Encapsulation: Private attributes for base and height
        self.__base = base
        self.__height = height
        self._name = "Triangle"

    def area(self):
        # Overriding the base class method
        return 0.5 * self.__base * self.__height

# Derived class for Circle
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__()
        # Encapsulation: Private attribute for radius
        self.__radius = radius
        self._name = "Circle"

    def area(self):
        # Overriding the base class method
        return math.pi * self.__radius ** 2

# Function to calculate the area of different polygons
def calculate_area(polygon):
    return polygon.area()

# Example usage
if __name__ == "__main__":
    # Create instances of different polygons
    rectangle = Rectangle(width=5, height=3)
    triangle = Triangle(base=4, height=6)
    circle = Circle(radius=2.5)

    # Calculate and print areas
    print(f"Area of {rectangle.get_name()}: {calculate_area(rectangle)}")
    print(f"Area of {triangle.get_name()}: {calculate_area(triangle)}")
    print(f"Area of {circle.get_name()}: {calculate_area(circle)}")
