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
# Purpose: This function, when given list[int], returns a list with the first element of each nensted list from an input. It also checks for empty lists.
# Input: list[int] , Output: list[int]
# Example Input: [[1,2], [3,4]] , Output Given the Input : [1,3]
# Name of function: first_element

def first_element(input: list[list[int]] ) -> list:
    newList = [x for x in input if x]
    return [x[0] for x in newList]
# Part 2
# Purpose: This function, when given list[Point] (from the point class), returns a list with the x-coordinate of each point.
# Input: list[int] , Output: list[int]
# Example Input: [[1,2], [3,4], [8,9], [10,12]] , Output Given the Input : [1,3,8,10]
# Name of function: x_coordinates

def x_coordinates(input: list[Point]):
    xcoordinates = [point for point in input]
    return [point[0] for point in xcoordinates]

# Part 3
# Purpose: This function, when given list[Point], returns all points from the input list in the first quadrant of the Cartesian plane.
# Input: list[int] , Output: list[int]
# Example Input: [Point(-5,5), Point(-1,-1), Point(4,4)] , Output Given the Input : [Point(4,4)]
# Name of function: are_in_positive_quadrant

def are_in_positive_quadrant(points: list[Point]) -> list[int]: # Changed input to "points" for clarity.
    newList = []
    for point in points:
        if point.x > 0 and point.y > 0:
            newList.append(point)
    else:
        return newList

# Part 4
# Purpose: This function, when given two parameters of type Point, returns the Euclidean distance as a float between two points.
# Input: float , Output: float
# Example Input: (Point(1,2)) , (Point(3,4)) , Output Given the Input : 2.8284271247461903
# Name of function: distance

def distance(point1: Point, point2: Point) -> float:
    euclidean_distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    return euclidean_distance

# Part 5
# Purpose: This function, when given two parameters of type Point, returns the Manhattan distance as a float between two points.
# Input: float , Output: float
# Example Input: (Point(6,6)) , Point(-2,5)) , Output Given the Input : 9
# Name of function: manhattan_distance

def manhattan_distance(point1: Point, point2: Point):
    manhattan_dist = (abs(point1.x - point2.x)) + (abs(point1.y - point2.y))
    return manhattan_dist

# Part 6
# Purpose: This function, when given a list[Point], returns a list with the distance from origin to each point in the list.
# Input: list[int] , Output: list[int]
# Example Input: [(Point(6,6))] , Output Given the Input : [8.48528137423857]
# Name of function:  distance_all

def distance1(point: Point) -> float:
    euclidean_distance = math.sqrt(point.x ** 2 + point.y ** 2)
    return euclidean_distance

def distance_all(point: list[Point]) -> list:
    return list(map(distance1, point))




