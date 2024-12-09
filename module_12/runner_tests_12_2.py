import runner_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = runner_2.Runner('Usain', 10)
        self.runner_andrew = runner_2.Runner('Andrew', 9)
        self.runner_nick = runner_2.Runner('Nick', 3)

    def test_race_1(self):
        race = runner_2.Tournament(90, self.runner_usain, self.runner_nick)
        self.__class__.all_results[1] = race.start()
        last_runner = self.__class__.all_results[max(self.__class__.all_results.keys())]
        self.assertTrue(last_runner[list(last_runner.keys())[-1]] == self.runner_nick)

    def test_race_2(self):
        race = runner_2.Tournament(90, self.runner_andrew, self.runner_nick)
        self.__class__.all_results[2] = race.start()
        last_runner = self.__class__.all_results[max(self.__class__.all_results.keys())]
        self.assertTrue(last_runner[list(last_runner.keys())[-1]] == self.runner_nick)

    def test_race_3(self):
        tournament = runner_2.Tournament(90, self.runner_usain, self.runner_andrew, self.runner_nick)
        self.__class__.all_results[3] = tournament.start()
        last_race = self.__class__.all_results[max(self.__class__.all_results.keys())]
        self.assertTrue(last_race[list(last_race.keys())[-1]] == self.runner_nick)

    def test_speed_order(self):
        # Меняем дистанцию на 50 и меняем очерёдность бегунов
        tournament = runner_2.Tournament(50, self.runner_usain, self.runner_nick, self.runner_andrew)
        result = tournament.start()
        runners_list = list(result.values())
        # Проверяем, что они финишировали в порядке убывания скорости
        self.assertEqual(runners_list[0].name, 'Usain')
        self.assertEqual(runners_list[1].name, 'Andrew')
        self.assertEqual(runners_list[2].name, 'Nick')


    @classmethod
    def tearDownClass(cls):
        result_format = {}
        for race_num in sorted(cls.all_results.keys()):
            result = cls.all_results[race_num]
            for place, runner in result.items():
                result_format[place] = runner.name
            print(result_format)


if __name__ == '__main__':
    unittest.main()