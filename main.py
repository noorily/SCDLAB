
# main.py
from shapes import Rectangle, Circle

def main():
    # Create a Rectangle with width 5 and height 7
    rect_a = Rectangle(5, 7)
    print("Rectangle a:")
    print(f"Area: {rect_a.area()}")
    print(f"Perimeter: {rect_a.perimeter()}")

    print("\nRectangle b:")
    # Create an empty Rectangle (width and height default to 0)
    rect_b = Rectangle()
    rect_b.width = 10
    rect_b.height = 20
    print(f"Width: {rect_b.width}")
    print(f"Height: {rect_b.height}")3.3
  
    print(f"Area: {rect_b.area()}")
    print(f"Perimeter: {rect_b.perimeter()}")

if __name__ == "__main__":
    main()
3.3
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
if __name__ == "__main__":
    # Create a Circle object with a given radius
    r = 7
    circle = Circle(r)
    circle_area = circle.calculate_area()
    circle_perimeter = circle.calculate_perimeter()

    # Print the results for the Circle
    print(f"Radius of the circle: {r}")
    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter: {circle_perimeter}")

    # Create a Rectangle object with given length and width
    l = 5
    w = 7
    rectangle = Rectangle(l, w)
    rectangle_area = rectangle.calculate_area()
    rectangle_perimeter = rectangle.calculate_perimeter()

    # Print the results for the Rectangle
    print(f"\nRectangle: Length = {l}, Width = {w}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Rectangle Perimeter: {rectangle_perimeter}")
  3.4
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
3.5
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Concrete class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Concrete class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Usage example
if __name__ == "__main__":
    circle = Circle(radius=5.0)
    rectangle = Rectangle(length=4.0, width=6.0)

    print(f"Circle area: {circle.calculate_area()}")
    print(f"Rectangle area: {rectangle.calculate_area()}")
3.7
# Example using a list of fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Count occurrences of 'apple'
apple_count = fruits.count('apple')
print(f"Number of 'apple' occurrences: {apple_count}")

# Find the index of 'banana'
banana_index = fruits.index('banana')
print(f"Index of 'banana': {banana_index}")

# Reverse the list
fruits.reverse()
print(f"Reversed list: {fruits}")

# Append 'grape' to the list
fruits.append('grape')
print(f"List after appending 'grape': {fruits}")

# Sort the list
fruits.sort()
print(f"Sorted list: {fruits}")

# Remove and return the last item ('pear')
removed_item = fruits.pop()
print(f"Removed item: {removed_item}")

# Note: Methods like insert, remove, or sort modify the list in place and return None.
# This design principle applies to all mutable data structures in Python.

