import runner
import unittest



class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = runner.Runner('Alex')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('Petr')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = runner.Runner('Roman')
        runner_4 = runner.Runner('Sergey')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3, runner_4)


if __name__ == '__main__':
    unittest.main()