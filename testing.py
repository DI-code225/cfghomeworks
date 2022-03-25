import unittest
from unittest import TestCase, main
from instructor_unit_test_file import red_or_blue

class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(num=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)

    def test_range_6_to_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)

    def test_range_2_to_5(self):
        expected = 'Blue'
        result = red_or_blue(num=2)
        self.assertEqual(expected, result)

    if __name__ == '__main__':
            main()

