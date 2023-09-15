# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

import shape_calculator

rect = shape_calculator.Rectangle(4, 3)
"""print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)"""

sq = shape_calculator.Square(2)
"""print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq) """


# Run unit tests automatically
main(module='test_module', exit=False)