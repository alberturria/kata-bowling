class Game:
    def __init__(self):
        self._strikes = []
        self._score = 0
        self._strike_bonus = False
        self._spare_bonus = False

    def roll(self, knocked_pins):
        self._strikes.append(knocked_pins)

    def score(self):
        if len(self._strikes) == 1:
            return self._strikes[0]
        index = 0
        while index < len(self._strikes):
            if self._strike_bonus:
                self._apply_strike_bonus(index)
            if self._spare_bonus:
                self._apply_spare_bonus(index)

            if index < len(self._strikes) - 1 and self._is_strike(index):
                self._strike_bonus = True
            elif index < len(self._strikes)-1 and self._is_spare(index):
                self._spare_bonus = True

            if index < len(self._strikes) - 1 and not self._strike_bonus:
                self._score += self._strikes[index + 1]

            self._score += self._strikes[index]

            index = self._get_updated_index(index)

        return self._score

    def _apply_strike_bonus(self, index):
        self._score += self._strikes[index] + self._strikes[index + 1]
        self._strike_bonus = False

    def _apply_spare_bonus(self, index):
        self._score += self._strikes[index]
        self._spare_bonus = False

    def _is_strike(self, index):
        return self._strikes[index] == 10

    def _is_spare(self, index):
        return self._strikes[index] + self._strikes[index + 1] == 10

    def _get_updated_index(self, index):
        if self._strike_bonus:
            index += 1
        else:
            index += 2

        return index




