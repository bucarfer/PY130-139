'''Triangles
Write a program to determine whether a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has exactly two sides of the same length.

A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0, and the sum of the lengths of any two sides must be greater than the length of the third side.'''

'''P
-triangle   -> each side greater than 0
            -> sum of any 2 sides > 3rd side
- 3 types of triangle (subclasses)
    1. equilateral -> all sides the same length
    2. isosceles -> 2 sides same length
    3. scalene -> all sides unequal
E
triangle(4, 3, 1) # no triangle
triangle(3, 3, 3)
triangle(5, 5, 2)
triangle()
D
class -> triangle
    subclasses ->  different types (wrong idea) -> instead of subclasses use a method
A
Generic algorithm
1. Build main class and check if arguments introduced meet triangle requirements
2. If not met return -> this is not a triangle
3. If triangle, determine what type and return the type

Constructor:
    -save the three sides
    -check all sides are greater than 0, raise an exception if not
    -use comparisons to check any 2 sides > 3td side

Method kind:
    -compare values of 3 sides
    -if all sides are equal -> equilateral
    -if 2 sides are equal -> isosceles
    -if all sides unequal -> scalene
C
'''

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self._is_valid():
            raise ValueError("Invalid triangle")

    @property
    def kind(self):
        unique_sides = len(set(self.sides))
        if unique_sides == 1:
            return "equilateral"
        elif unique_sides == 2:
            return "isosceles"
        else:
            return "scalene"

    def _is_valid(self):
        return (
            all(side > 0 for side in self.sides)
            and self.sides[0] < (self.sides[1] + self.sides[2])
            and self.sides[1] < (self.sides[2] + self.sides[0])
            and self.sides[2] < (self.sides[0] + self.sides[1])
        )

    ### LS alternative for _is_valid
    # def _is_valid(self):
    #     a, b, c = sorted(self.sides)
    #     return a > 0 and  a + b > c

# try:
#     tr1 =  Triangle(4, 3, 1) # no triangle
#     print(tr1.kind)
# except ValueError as e:
#     print(e)

# tr2 =  Triangle(3, 3, 3)
# print(tr2.kind)
# tr3 =  Triangle(5, 5, 2)
# print(tr3.kind)
# tr4 =  Triangle(4, 2, 5)
# print(tr4.kind)