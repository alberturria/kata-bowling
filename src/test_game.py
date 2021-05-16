import unittest

from src.game import Game


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_when_rolling_without_a_spare_then_the_score_is_updated_by_the_number_of_knocked_pins(self):
        expected_score = 5

        self.game.roll(5)

        self.assertEqual(self.game.score(), expected_score, 'Should\'ve set the proper score')

    def test_when_running_a_whole_game_with_a_spare_bonus_frames_then_the_game_score_is_the_correct_one(self):
        expected_score = 86

        for index in range(2):
            self.game.roll(5)

        for index in range(18):
            self.game.roll(4)

        self.assertEqual(self.game.score(), expected_score, 'Should\'ve returned the correct score')

    def test_when_running_a_strike_then_the_game_score_is_the_correct_one(self):
        expected_score = 90

        self.game.roll(10)

        for index in range(18):
            self.game.roll(4)

        self.assertEqual(self.game.score(), expected_score, 'Should\'ve returned the correct score')

    def test_when_running_all_strikes_then_the_correct_score_is_returned(self):
        expected_score = 300

        for index in range(12):
            self.game.roll(10)

        self.assertEqual(self.game.score(), expected_score, 'Should\'ve returned the correct score')