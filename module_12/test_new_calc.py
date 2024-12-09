import calc
import unittest

class NewCalcTest(unittest.TestCase):
    @unittest.skip("не используется")
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    @unittest.skipIf(8 > 2, 'Не повезло')
    def test_pow(self):
        self.assertEqual(calc.pow(8, 5), 32768)


if __name__ == '__main__':
    unittest.main()