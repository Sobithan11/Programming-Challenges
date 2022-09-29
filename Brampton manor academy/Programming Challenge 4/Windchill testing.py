import unittest

from WindChill import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(Windchill(65,32),62.27398227950922 )



if __name__ == '__main__':
    unittest.main()