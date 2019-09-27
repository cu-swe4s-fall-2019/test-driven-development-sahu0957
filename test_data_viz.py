import unittest
import data_viz
import random
import os
from os import path


class TestDataViz(unittest.TestCase):

    def test_data_viz_empty_list_boxplot(self):
        L = []
        r = data_viz.boxplot(L, 'boxplot')
        self.assertEqual(r, None)

    def test_data_viz_constant_boxplot(self):
        L = [1, 2, 3, 4, 5]
        data_viz.boxplot(L, 'boxplot.png')
        self.assertTrue(path.exists("boxplot.png"))

    def test_data_viz_nonnumber_boxplot(self):
        L = ['foo', 'bar']
        with self.assertRaises(TypeError) as ex:
            data_viz.boxplot(L, 'boxplot.png')

    def test_data_viz_float_boxplot(self):
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.boxplot(L, 'boxplot.png')
        self.assertTrue(path.exists("boxplot.png"))

    def test_data_viz_empty_list_histogram(self):
        L = []
        r = data_viz.histogram(L, 'histogram.png')
        self.assertEqual(r, None)

    def test_data_viz_constant_histogram(self):
        L = [1, 2, 3, 4, 5]
        data_viz.histogram(L, 'histogram.png')
        self.assertTrue(path.exists("histogram.png"))

    def test_data_viz_float_histogram(self):
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.histogram(L, 'histogram.png')
        self.assertTrue(path.exists("histogram.png"))

    def test_data_viz_empty_list_combo(self):
        L = []
        r = data_viz.boxplot(L, 'combo.png')
        self.assertEqual(r, None)

    def test_data_viz_constant_combo(self):
        L = [1, 2, 3, 4, 5]
        data_viz.combo(L, 'combo.png')
        self.assertTrue(path.exists("combo.png"))

    def test_data_viz_nonnumber_combo(self):
        L = ['foo', 'bar']
        with self.assertRaises(TypeError) as ex:
            data_viz.combo(L, 'combo.png')

    def test_data_viz_float_combo(self):
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.combo(L, 'combo.png')
        self.assertTrue(path.exists("combo.png"))

    def tearDown(self):
        if path.exists("boxplot.png"):
            os.remove("boxplot.png")
        if path.exists("histogram.png"):
            os.remove("histogram.png")
        if path.exists("combo.png"):
            os.remove("combo.png")


if __name__ == '__main__':
    unittest.main()
