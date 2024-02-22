import math

class Shape:
    def __init__(self):
        pass  # Placeholder constructor

    def area(self):
        pass  # Placeholder method for calculating area

    def perimeter(self):
        pass  # Placeholder method for calculating perimeter

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
2.1

class Shape:
    def __init__(self):
        self.name = "Shape"

    def __str__(self):
        return f"I am a {self.name} defined as {type(self).__name__}"

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.name = "Rectangle"
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()}"

# Example usage:
rectangle = Rectangle(length=10, width=5)
circle = Circle(radius=7)

print(rectangle)  # Output: "I am a Rectangle defined as Rectangle with an area of 50"
print(circle)     # Output: "I am a Circle defined as Circle with an area of 153.93804002589985"
2.2
class Shape:
    def __init__(self):
        self._name = "Shape"  # Private attribute with a single underscore

    def __str__(self):
        return f"I am a {self._name} defined as {type(self).__name__}"

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self._name = "Rectangle"
        self._length = length  # Private attribute for length
        self._width = width    # Private attribute for width

    def area(self):
        return self._length * self._width

    # Getter methods
    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    # Setter methods
    def set_length(self, length):
        self._length = length

    def set_width(self, width):
        self._width = width

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._name = "Circle"
        self._radius = radius  # Private attribute for radius

    def area(self):
        import math
        return math.pi * self._radius ** 2

    # Getter method
    def get_radius(self):
        return self._radius

    # Setter method
    def set_radius(self, radius):
        self._radius = radius

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()}"

# Example usage:
rectangle = Rectangle(length=10, width=5)
circle = Circle(radius=7)

print(rectangle)  # Output: "I am a Rectangle defined as Rectangle with an area of 50"
print(circle)     # Output: "I am a Circle defined as Circle with an area of 153.93804002589985"

# Accessing and modifying attributes using getter and setter methods
rectangle.set_length(12)
rectangle.set_width(6)
print(f"Modified rectangle area: {rectangle.area()}")

circle.set_radius(8)
print(f"Modified circle area: {circle.area()}")
2.3
class Shape:
    def __init__(self):
        self._name = "Shape"

    def __str__(self):
        return f"I am a {self._name} defined as {type(self).__name__}"

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self._name = "Rectangle"
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()} and a perimeter of {self.perimeter()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._name = "Circle"
        self._radius = radius

    def area(self):
        import math
        return math.pi * self._radius ** 2

    def circumference(self):
        return 2 * math.pi * self._radius

    def __str__(self):
        return f"{super().__str__()} with an area of {self.area()} and a circumference of {self.circumference()}"

# Example usage:
rectangle = Rectangle(length=10, width=5)
circle = Circle(radius=7)

print(rectangle)  # Output: "I am a Rectangle defined as Rectangle with an area of 50 and a perimeter of 30"
print(circle)     # Output: "I am a Circle defined as Circle with an area of 153.93804002589985 and a circumference of 43.982297150257104"
