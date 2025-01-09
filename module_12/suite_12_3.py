import unittest
import stamina_tests_12_1, runner_tests_12_2

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(stamina_tests_12_1.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)
