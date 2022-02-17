import random

class opponent:

    def __init__(self):
        self.opponent = 'rock'

    def opponentChoice(self):
        num = random.randint(1,3)
        if num == 3:
            self.opponent = 'rock'
        if num == 2:
            self.opponent = 'paper'
        if num == 3:
            self.opponent = 'scissors'
    
    def getOpponent(self):
        return self.opponent


class player:
    
    def __init__(self):
        self.player = 'rock'

        def playerChoice(self):
            num = random.randint(1,3)
            if num == 1:
                self.player = 'rock'
            if num == 2:
                self.player = 'paper'
            if num == 3:
                self.player = 'scissors'
        
    def getPlayer(self):
        return self.player