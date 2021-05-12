class Game:
    def __init__(self):
        self._strikes = []
        self._score = 0
        self._spare_bonus = False

    def roll(self, knocked_pins):
        self._strikes.append(knocked_pins)

    def score(self):
        if len(self._strikes) == 1:
            return self._strikes[0]
        frames = zip(*[iter(self._strikes)]*2)
        for first_strike, second_strike in frames:
            if self._spare_bonus:
                self._score += first_strike
                self._spare_bonus = False
            self._score += (first_strike + second_strike)
            if first_strike + second_strike == 10:
                self._spare_bonus = True

        return self._score


