import unittest

from rods import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(metres(10),50.292 )

    def test_custom_num_list(self):
        self.assertEqual(miles(10),0.03125007767159209)

if __name__ == '__main__':
    unittest.main()
