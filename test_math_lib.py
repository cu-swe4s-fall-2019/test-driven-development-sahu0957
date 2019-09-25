import unittest
import math_lib


class TestMathLib(unittest.TestCase):
   def test_list_mean_empty_list(self):
       r = math_lib.list_mean([])
       self.assertEqual(r, None)

    
   def test_list_mean_constant(self):
       r = math_lib.list_mean([1,1,1,1])
       self.assertEqual(r, 1)


if __name__ == '__main__':
    unittest.main()
