import data

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
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def x_coordinates(input: list[Point]):
    xcoordinates = [point for point in input]
    return [point[0] for point in xcoordinates]

# Part 3


# Part 4


# Part 5


# Part 6


