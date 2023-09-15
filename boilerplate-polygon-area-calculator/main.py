from unittest import main
import shape_calculator

#Constructor
rect = shape_calculator.Rectangle(4, 3)
sq = shape_calculator.Square(2)

# To string
print(rect)
print(sq)

print("\nRectangle area:" + str(rect.get_area()))
print("\nSquare area:" + str(sq.get_area()))

rect.set_width(5)
print("\nRectangle perimeter:" + str(rect.get_perimeter()))

sq.set_side(4)
print("\nSquare diagonal:" + str(sq.get_diagonal()))

print("\n Square picture:")
print(sq.get_picture())
print("\n Rectangle picture:")
print(rect.get_picture())
