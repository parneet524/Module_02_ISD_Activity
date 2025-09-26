""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from shape import *  # Shape, Triangle, Rectangle

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []  # type: list[Shape]


    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        tri1 = Triangle("red", 5, 6, 7)
        shapes.append(tri1)
    except Exception as e:
        print(e)


    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rect1 = Rectangle("blue", 3, 4)
        shapes.append(rect1)
    except Exception as e:
        print(e)



    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        tri2 = Triangle("green", 3, 4, 5)  # classic 3-4-5
        shapes.append(tri2)
    except Exception as e:
        print(e)

    try:
        rect2 = Rectangle("yellow", 10, 2)
        shapes.append(rect2)
    except Exception as e:
        print(e)

    try:
        tri3 = Triangle("purple", 8, 9, 10)
        shapes.append(tri3)
    except Exception as e:
        print(e)



    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for idx, shp in enumerate(shapes, start=1):
        print(f"\n-- Shape {idx} --")
        # __str__ itself is safe, but keep consistent try/except practice:
        try:
            print(shp)
        except Exception as e:
            print(e)

        try:
            area = shp.calculate_area()
            print(f"Area: {area:.2f}")
        except Exception as e:
            print(e)

        try:
            perim = shp.calculate_perimeter()
            print(f"Perimeter: {perim:.2f}")
        except Exception as e:
            print(e)


    # *** END PART 1 ***


if __name__ == "__main__":
    main()