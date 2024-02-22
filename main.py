
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

