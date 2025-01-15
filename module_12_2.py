import runner_and_tournament as rt
import unittest


@unittest.skipIf(True, "Тесты в этом кейсе заморожены")
class TournamentTest(unittest.TestCase):

    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.husein = rt.Runner("Усэйн", 10)
        self.andrey = rt.Runner("Андрей", 9)
        self.nick = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for tkey, tvalue in cls.all_results.items():
            print(f'{tkey}')
            for rkey, rvalue in tvalue.items():
                result[rkey] = str(rvalue.name)
            print(result)

    def test_husein_nick(self):
        race = rt.Tournament(90, self.husein, self.nick)
        results = race.start()
        self.assertTrue('Ник' == results[len(results)].name)
        self.all_results[f'Результат {self.husein} и {self.nick}'] = results

    def test_andrey_nick(self):
        race = rt.Tournament(90, self.andrey, self.nick)
        results = race.start()
        self.assertTrue('Ник' == results[len(results)].name)
        self.all_results[f'Результат {self.andrey} и {self.nick}'] = results

    def test_husein_andrey_nick(self):
        race = rt.Tournament(90, self.husein, self.andrey, self.nick)
        results = race.start()
        self.assertTrue('Ник' == results[len(results)].name)
        self.all_results[f'Результат {self.husein}, {self.andrey} и {self.nick}'] = results

    def test_nick_andrey_husein_8(self):
        race = rt.Tournament(9, self.nick, self.andrey, self.husein)
        results = race.start()
        self.assertTrue('Ник' == results[len(results)].name)
        self.all_results[f'Результат {self.nick}, {self.andrey} и {self.husein}'] = results


if __name__ == '__main__':
    unittest.main()