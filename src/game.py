class Game:
    def __init__(self):
        self._score = 0

    def roll(self, knocked_pins):
        self._score += knocked_pins

    def score(self):
        return self._score