import data
import math

class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))

# Write your functions for each part in the space below.

#Briefly state the purpose of the function, including input and output.
#Identify the representation of the data to be used in the computation.
#Name and template the function.
#Do computation by hand and write tests.
# Complete the function implementation.

# Part 1
def first_element(input: list[list[int]] ) -> list:
    newList = [x for x in input if x]
    return [x[0] for x in newList]
# Part 2
def x_coordinates(input: list[Point]):
    xcoordinates = [point for point in input]
    return [point[0] for point in xcoordinates]

# Part 3
def are_in_positive_quadrant(points: list[Point]) -> list[int]: # Changed input to "points" for clarity.
    newList = []
    for point in points:
        if point.x > 0 and point.y > 0:
            newList.append(point)
    else:
        return newList

# Part 4
def distance(point1: Point, point2: Point) -> float:
    euclidean_distance = math.dist(point1 , point2)
    return euclidean_distance




# Part 5


# Part 6


