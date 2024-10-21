import data
import lab4
import unittest


# Write your test cases for each part below.

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


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
