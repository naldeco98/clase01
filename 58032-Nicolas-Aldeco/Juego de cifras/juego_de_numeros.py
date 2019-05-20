import random

class Game():

    def __init__(self):
        self.game_status = True
        self.tries = 0

class HumanVsComputer(Game):

    def __init__(self):
        super().__init__()
        self.number = ''
        self.number += str(random.randint(0,9))
        self.number += str(random.randint(0,9))
        self.number += str(random.randint(0,9))
        self.number += str(random.randint(0,9))
        self.good = 0
        self.regular = 0
        self.bad = 0

    def play(self,guest):
        ct = 0
        ans = ''
        self.bad = 0
        self.regular = 0
        self.good = 0
        while ct != 4:
            if self.number.find(guest[ct]) == -1:
                self.bad += 1
            if self.number.find(self.number[ct]) == self.number.find(guest[ct]):
                self.good += 1
            if self.number.find(guest[ct]) != -1 and self.number.find(self.number[ct]) != self.number.find(guest[ct]):
                self.regular += 1
            ct += 1
        if self.bad != 0:
            ans += str(self.bad) + 'B'
        if self.good != 0:
            ans += str(self.good) + 'G'
        if self.regular != 0:
            ans += str(self.regular) + 'R'
        self.tries += 1
        if self.good == 4:
            self.game_status = False
        return ans

class ComputerVsHuman(Game):

    def __init__(self):
        super().__init__()

    def play(self,)