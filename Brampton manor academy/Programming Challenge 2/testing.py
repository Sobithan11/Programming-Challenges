import unittest

from Richter import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(energy(3),1995262314.9688828 )

    def test_custom_num_list(self):
        self.assertEqual(tons_of_tnt(3),0.47687913837688406)

if __name__ == '__main__':
    unittest.main()
