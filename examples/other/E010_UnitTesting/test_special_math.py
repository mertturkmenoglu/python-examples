from unittest import TestCase
from E010_UnitTesting import special_math


class TestSpecialMath(TestCase):
    def test_add_one(self):
        expected = 1
        actual = special_math.add_one(0)
        self.assertEqual(expected, actual, "Add one failed")

    def test_add_something(self):
        expected = 5
        actual = special_math.add_something(2, 3)
        self.assertEqual(expected, actual, "Add something failed")

    def test_increment(self):
        expected = 3
        actual = special_math.increment(2)
        self.assertEqual(expected, actual, "Increment failed")
