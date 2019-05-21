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
        if self.good != 0:
            ans += str(self.good) + 'G'
        if self.regular != 0:
            ans += str(self.regular) + 'R'
        self.tries += 1
        if self.bad == 4:
            return 'All Bads try other number.'
        if self.good == 4:
            self.game_status = False
            return 'All Goods, you win!'
        return 'You have '+ ans

class ComputerVsHuman(Game):

    def __init__(self):guest_list_all_digits = ['0000'guest_list_all_digits = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999'],'1111','2222','3333','4444','5555','6666','7777','8888','9999']
        super().__init__()
        self.guest = ''
        self.guest_list_all_digits = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
        self.guest2 = ['','','','']
        self.guest3 = []
        self.clue = ''
        self.ct = 0
        self.ct2 = 0
    def play(self):  
        if self.tries < 10:  
            self.guest = self.guest_list_all_digits[self.ct]
            self.ct += 1
            self.tries += 1
        if self.clue == '1G3R':        
            self.guest2[self.ct2] = self.guest_list_all_digits[self.ct2 + 1]
            guest2 = self.guest2[self.ct2]
            guest2[] =
            self.guest2.remove[self.ct2]
            self.guest2.insert(self.ct2,guest2)
            self.ct2 += 1
        if self.clue == '4G':
            return 'I win your number was '+ self.guest
        return 'Is your number '+ self.guest +'?'

    def inputx(self):
        self.clue = input('>>')
        return