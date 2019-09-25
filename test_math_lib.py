import unittest
import math_lib
import random
import statistics
import math

class TestMathLib(unittest.TestCase):

    def test_list_mean_empty_list(self):
       r = math_lib.list_mean([])
       self.assertEqual(r, None)


    def test_list_mean_constant(self):
       r = math_lib.list_mean([1,1,1,1])
       self.assertEqual(r, 1)

    def test_list_mean_rand_integers(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0,100))

        r = math_lib.list_mean(L)
        e = statistics.mean(L)
        self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.random())

        r = math_lib.list_mean(L)
        e = statistics.mean(L)
        self.assertTrue(math.isclose(r, e))

if __name__ == '__main__':
    unittest.main()
