import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', 1, 2), 3)
    def test_sub(self):
        self.assertEqual(calculate('sub', 5, 3), 2)
    def test_mul(self):
        self.assertEqual(calculate('mul', 2, 4), 8)
    def test_div(self):
        self.assertAlmostEqual(calculate('div', 10, 4), 2.5)

if __name__ == '__main__':
    unittest.main()
