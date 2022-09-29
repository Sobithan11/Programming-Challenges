import unittest

from the99trick import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(game(6,98),"I said the answer was 6 and the calculation result is 6")

    def test_custom_num_list(self):
        self.assertEqual(5)

if __name__ == '__main__':
    unittest.main()