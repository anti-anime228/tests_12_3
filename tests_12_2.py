import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers




class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key1, value1 in cls.all_results.items():
            print(f'Тест: {key1}')
            for key2, valu2 in value1.items():
                print(f'{key2}: {valu2.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_vs_nick(self):
        tournament_usain_vs_nick = Tournament(90, self.usain, self.nick)
        start_test = tournament_usain_vs_nick.start()
        self.all_results['tournament_usain_vs_nick'] = start_test

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrew_vs_nick(self):
        tournament_andrew_vs_nick = Tournament(90, self.andrew, self.nick)
        start_test = tournament_andrew_vs_nick.start()
        self.all_results['tournament_andrew_vs_nick'] = start_test

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_all(self):
        tournament_all = Tournament(90, self.usain, self.andrew, self.nick)
        start_test = tournament_all.start()
        self.all_results['tournament_all'] = start_test

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_short(self):
        short = Tournament(6, self.usain, self.andrew, self.nick)
        start_short = short.start()
        self.all_results['test_short'] = start_short

if __name__ == '__main__':
    unittest.main()


