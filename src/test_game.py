import unittest

from src.game import Game


class GameTestCase(unittest.TestCase):
    def test_when_rolling_without_a_then_the_score_is_updated_by_the_number_of_knocked_pins(self):
        expected_score = 5
        game = Game()

        game.roll(5)

        self.assertEquals(game.score(), expected_score, 'Should\'ve set the proper score')