import calc
import unittest

class CalcTest(unittest.TestCase):
    # запуск перед каждым тест-кейсом
    def setUp(self):
        print('setup')

    # запуск ОДИН раз перед всеми тест-кейсами
    @classmethod
    def setUpClass(cls):
        print('MegaSetup')

    # запуск после каждого тест-кейса
    def tearDown(self):
        pass

    # запуск ОДИН раз после всех тест-кейсов
    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calc.add(5, 20), 25)

    def test_sub(self):
        """
        Test for sub function in calculator
        :return:
        """
        self.assertEqual(calc.sub(45, 10), 35)

    def test_mul(self):
        """
        Test for mul function in calculator
        :return:
        """
        self.assertEqual(calc.mul(5, 20), 100)

    def test_div(self):
        """
        Test for div function in calculator
        :return:
        """
        self.assertEqual(calc.div(20, 5), 4)


if __name__ == '__main__':
    unittest.main()