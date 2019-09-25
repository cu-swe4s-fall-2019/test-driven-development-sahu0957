import unittest
import math_lib


class TestMathLib(unittest.TestCase):
   def test_list_mean_empty_list(self):
       r = math_lib.list_mean([])
       self.assertEqual(r, None) 


if __name__ == '__main__':
    unittest.main()
