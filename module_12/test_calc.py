import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 20), 25)
    def test_sub(self):
        self.assertEqual(calc.sub(45, 10), 35)
    def test_mul(self):
        self.assertEqual(calc.mul(5, 20), 100)
    def test_div(self):
        self.assertEqual(calc.div(20, 5), 4)


if __name__ == '__main__':
    unittest.main()