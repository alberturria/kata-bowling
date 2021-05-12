import unittest

from src.game import Game


class GameTestCase(unittest.TestCase):
    def test_when_rolling_without_a_spare_then_the_score_is_updated_by_the_number_of_knocked_pins(self):
        expected_score = 5
        game = Game()

        game.roll(5)

        self.assertEquals(game.score(), expected_score, 'Should\'ve set the proper score')

    def test_when_running_a_whole_game_with_a_spare_bonus_frames_then_the_game_score_is_the_correct_one(self):
        expected_score = 86
        game = Game()

        for index in range(2):
            game.roll(5)

        for index in range(18):
            game.roll(4)

        self.assertEquals(game.score(), expected_score, 'Should\'ve returned the correct score')
