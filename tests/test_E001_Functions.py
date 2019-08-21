import unittest
from E001_Functions import main


class FunctionsTest(unittest.TestCase):
    def test_find_square_area(self):
        assert(main.find_square_area(4) == 16)


if __name__ == '__main__':
    unittest.main()
