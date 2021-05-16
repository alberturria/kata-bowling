class Game:
    def __init__(self):
        self._strikes = []
        self._score = 0
        self._strike_bonus = False
        self._spare_bonus = False

    def roll(self, knocked_pins):
        self._strikes.append(knocked_pins)

    def score(self):
        index = 0
        while index < len(self._strikes):
            if self._is_strike(index):
                self._apply_strike_bonus(index)
            elif self._is_spare(index):
                self._apply_spare_bonus(index)
            else:
                self._score += self._strikes[index]

            index = self._get_updated_index(index)

        return self._score

    def _apply_strike_bonus(self, index):
        if len(self._strikes) > index + 2:
            self._score += self._strikes[index] + self._strikes[index + 1] + self._strikes[index + 2]

    def _apply_spare_bonus(self, index):
        self._score += self._strikes[index] + self._strikes[index + 1] + self._strikes[index + 2]

    def _is_strike(self, index):
        return self._strikes[index] == 10

    def _is_spare(self, index):
        return self._strikes[index] + self._strikes[index + 1] == 10 if len(self._strikes) > index + 1 else False

    def _get_updated_index(self, index):
        if self._is_spare(index):
            index += 2
        else:
            index += 1

        return index




