#necessary library
import random
#opponent class
class Opponent:
    #beginning value
    def __init__(self):
        self.opponent = 'rock'
    #determine opponents choice
    def opponentChoice(self):
        num = random.randint(1,3)
        if num == 1:
            self.opponent = 'rock'
        if num == 2:
            self.opponent = 'paper'
        if num == 3:
            self.opponent = 'scissors'
    #get opponents choice
    def getOpponent(self):
        return self.opponent

#player class
class Player:
    #beginning value
    def __init__(self):
        self.player = 'rock'
    #determine players choice
    def playerChoice(self):
        choice=0
        try:
            while choice not in range(1,4):
                choice = int(input('1 = Rock, 2 = Paper, 3 = Scissors '))
        except:
            pass
        if choice == 1:
            self.player = 'rock'
        if choice == 2:
            self.player = 'paper'
        if choice == 3:
            self.player = 'scissors'
    #get players choice  
    def getPlayer(self):
        return self.player