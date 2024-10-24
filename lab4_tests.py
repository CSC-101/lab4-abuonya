import data
import lab4
import unittest
import math


# Write your test cases for each part below.
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

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[1,2], [], [3,4]]
        result = lab4.first_element(input)
        expected = [1,3]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates(self):
        input = [[1,2], [3,4]]
        result = lab4.x_coordinates(input)
        expected = [1,3]
        self.assertEqual(expected, result)

    def test_x_coordinates2(self):
        input = [[1,2], [3,4], [8,9], [10,12]]
        result = lab4.x_coordinates(input)
        expected = [1,3,8,10]
        self.assertEqual(expected, result)

    # Part 3
    #POSTIVE POINTS ONLY
    def test_are_in_positive_quadrant1(self):
        input = [Point(1,2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(1,2)]
        self.assertEqual(expected, result)

    # some different quadrants now...
    def test_are_in_positive_quadrant2(self):
        input = [Point(-5,5), Point(-1,-1), Point(4,4)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(4,4)]
        self.assertEqual(expected, result)
    # Part 4
    def test_distance1(self):
        input = (Point(1,2))
        another = (Point(3,4))
        result = lab4.distance(input, another)
        expected = 2.8284271247461903
        self.assertEqual(expected, result)

    def test_distance2(self):
        input = (Point(-2,4))
        another = (Point(5,-5))
        result = lab4.distance(input, another)
        expected = 11.40175425099138
        self.assertEqual(expected, result)
    # Part 5
    def test_manhattan_distance1(self):
        input = (Point(1,2))
        another = (Point(3,4))
        result = lab4.manhattan_distance(input, another)
        expected = 4
        self.assertEqual(expected, result)

    def test_manhattan_distance2(self):
        input = (Point(6,6))
        another = (Point(-2,5))
        result = lab4.manhattan_distance(input, another)
        expected = 9
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all1(self):
        input = [(Point(6,6))]
        result = lab4.distance_all(input)
        expected = [8.48528137423857]
        self.assertEqual(expected, result)

    def test_distance_all2(self):
        input = [(Point(-5,-11))]
        result = lab4.distance_all(input)
        expected = [12.083045973594572]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
