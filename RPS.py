import RPSclass as r
import time

def main():
    opponent = r.Opponent()
    player = r.Player()
    mainMenu()
    play(opponent,player)


def mainMenu():
    print('*'*40)
    print(format('Welcome to Rock Paper scissors!','^40'), '\n')
    time.sleep(2)
    cont = input(format('Enter 1 for the rules or press enter to play\n', '^40'))
    if cont != '':
        rules()
    print('*'*40)


def rules():
    print('*'*40)
    print('1. The goal of the game is to win 5 times!')
    time.sleep(4)
    print('2. To play, type in your selection of \nrock, paper, or scissors')
    time.sleep(4)
    print('3. Rock beats scissors, scissors beats \npaper, and paper beats rock.')
    time.sleep(4)


def play(opponent,player):
    playerWins = 0
    opponentWins = 0

    while True:
        if opponentWins == 5:
            break
        if playerWins == 5:
            break
        opponent.opponentChoice()
        player.playerChoice()
        opp = opponent.getOpponent()
        pla = player.getPlayer()
        print('Your opponent chose:',opp, '\n')
        time.sleep(2)
        print('You chose:', pla, '\n')
        time.sleep(2)

        if opp == pla:
            print('The result is a tie!\n')
        elif opp == 'rock' and pla == 'paper':
            print('You win this round!\n')
            playerWins+=1
        elif opp == 'rock' and pla == 'scissors':
            print('You lost this round!\n')
            opponentWins+=1
        elif opp == 'paper' and pla == 'scissors':
            print('You win this round!\n')
            playerWins+=1
        elif opp == 'paper' and pla == 'rock':
            print('You lost this round!\n')
            opponentWins+=1
        elif opp == 'scissors' and pla == 'rock':
            print('You win this round!\n')
            playerWins+=1
        elif opp == 'scissors' and pla == 'paper':
            print('You lost this round!\n')
            opponentWins+=1
        
        print('Opponent:', opponentWins)
        print('Player:',playerWins)
        print()

    if playerWins == 5:
        print(format('Congratualtions!', '^40'))
        print()
        print(format('You won the game!', '^40'))
        print()
    
    if opponentWins == 5:
        print(format('You lost the game.', '^40'))
        print()
        print(format('Maybe try harder next time!', '^40'))
        print()

    cont = input('Would you like to play again(y/n)? ')
    if cont[0].lower() == 'y':
        main()
        

main()