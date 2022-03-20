#!/usr/bin/python

import random
import os


class Style:
        RESET = '\033[0m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        underLine = '\033[4m'


class Scores:
	def stats(self):
		print(f'Games Won: {self.gamesWon}')
		print(f'Games Lost: {self.gamesLost}')
		print(f'Games Tied: {self.gamesTied}')

	gamesWon = 0
	gamesLost = 0
	gamesTied = 0


playerScores = Scores()
computerScores = Scores()

def main():
        #Select Game Version to Play
        gameVersion = 0
        while gameVersion != 1 or gameVersion != 2:
                gameVersion = int(input('1: Classic Rock, Paper, Scissors \n' \
                        '2: Rock, Paper, Scissors, Lizard, Spock \n' \
                        'Selection: '))

                if gameVersion == 1:
                        classicGame()
                        break
                elif gameVersion == 2:
                        bigBang()
                        break
                else:
                        clearConsole()
                        print('Please Enter a Valid Selection')
                        main()


def classicGame():
        #Setup Classic
        clearConsole()

	#Choices tat are applicable
        choices = ['rock', 'paper', 'scissors']
        print(Style.YELLOW + 'Rock Paper Scirrors' + Style.RESET)
        rules('Classic')
        input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
        clearConsole()

        print(Style.YELLOW + 'Rock Paper Scissors' + Style.RESET)
        totalGames = int(input('How Many Games to Play?: '))
        playGame('Classic', choices, totalGames)


def bigBang():
        #Setup BigBang
        clearConsole()

	#Choices that are applicable 
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        print(Style.YELLOW + 'Big Bang' + Style.RESET)
        rules('BigBang')
        input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
        clearConsole()

        print(Style.YELLOW + 'Big Bang' + Style.RESET)
        totalGames = int(input('How Many Games to Play?: '))
        playGame('BigBang', choices, totalGames)


def playGame(gameType, choices, totalGames):
        clearConsole()

	#Play Classic
        if gameType == 'Classic':
                gameCalculations(choices, totalGames)

	#Play BigBangTheory Version
        if gameType == 'BigBang':
                gameCalculations(choices, totalGames)


def rules(gameType):
        #Define Rules for Game Types
        if gameType == 'Classic':
                print(Style.GREEN + 'Rock' + Style.RESET + ' beats ' + Style.RED + 'Scissors \n' \
                        + Style.GREEN + 'Paper' + Style.RESET + ' beats ' + Style.RED + 'Rock \n' \
                        + Style.GREEN + 'Scissors' + Style.RESET + ' beats ' + Style.RED + 'Paper \n\n')
        if gameType == 'BigBang':
                print(Style.GREEN + 'Scissors' + Style.RESET + ' cuts ' + Style.RED + 'Paper \n' \
                        + Style.GREEN + 'Paper' + Style.RESET + ' covers ' + Style.RED + 'Rock \n' \
                        + Style.GREEN + 'Rock' + Style.RESET + ' crushes ' + Style.RED + 'Lizard \n' \
                        + Style.GREEN + 'Lizard' + Style.RESET + ' poisons ' + Style.RED + 'Spock \n' \
                        + Style.GREEN + 'Spock' + Style.RESET + ' smashes ' + Style.RED + 'Scissors \n' \
                        + Style.GREEN + 'Scissors' + Style.RESET + ' decapites ' + Style.RED + 'Lizard \n' \
                        + Style.GREEN + 'Lizard' + Style.RESET + ' eats ' + Style.RED + 'Paper \n' \
                        + Style.GREEN + 'Paper' + Style.RESET + ' disaproves ' + Style.RED + 'Spock \n' \
                        + Style.GREEN + 'Spock' + Style.RESET + ' vaporizes ' + Style.RED + 'Rock \n' \
                        + Style.RESET + 'And as it always has \n' \
                        + Style.GREEN + 'Rock' + Style.RESET + ' crushes ' + Style.RED + 'Scissors \n\n')


def gameCalculations(choices, totalGames):
	for game in range(1, totalGames + 1, 1):
		clearConsole()

		print(f'Playing Game {game} of {totalGames}')

		userAction = input('Please Enter Your Move: ').lower
		computerAction = random.choice(choices)

		if userAction == computerAction:
			print('It\'s a Tie')
			playerScores.gamesTied = playerScores.gamesTied + 1
			computer.Scores.gamesTied = computerScores.gamesTied + 1
		elif userAction == 'rock':
			if computerAction == 'paper':
				print(Style.RED + 'Paper covers Rock!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'scissors':
				print(Style.GREEN + 'Rock smashes Scissors!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScoores.gamesLost = computerScores.gamesLost + 1
			elif computerAction == 'lizard':
				print(Style.GREEN + 'Rock crushes Lizard!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
			else:
				print(Style.RED + 'Spock vaporizes Rock!' + Style.RESET)
				playerScores.gamesLost = player.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
		elif userAction == 'paper':
			if computerAction == 'rock':
				print(Style.GREEN + 'Paper covers Rock!' + Style.RESET)
				playerScores.gamesWon = playerScores.GamesWon + 1
				computerScores.gamesLost = computerScores.GamesLost + 1
			elif computerAction == 'scissors':
				print(Style.RED + 'Scissors cuts Paper!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'lizard':
				print(Style.RED + 'Lizard eats Paper!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			else:
				print(Style.GREEN + 'Paper disaproves Spock!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
		elif userAction == 'scissors':
			if computerAction == 'rock':
				print(Style.RED + 'Rock smashes Scissors!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'paper':
				print(Style.GREEN + 'Scissors cuts Paper!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
			elif computerAction == 'lizard':
				print(Style.GREEN + 'Scissors decapitates Lizard!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.GamesLost + 1
			else:
				print(Style.RED + 'Spock smashes Scissors!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
		elif userAction == 'lizard':
			if computerAction == 'rock':
				print(Style.RED + 'Rock crushes Lizard' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'paper':
				print(Style.RED + 'Lizard  eats Paper!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'scissors':
				print(Style.RED + 'Scissors decapitates Lizard!' + Style.RESET)
				playerScores.GamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			else:
				print(Style.GREEN + 'Lizard poisons Spock' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
		elif userAction == 'spock':
			if computerAction == 'rock':
				print(Style.GREEN + 'Spock vaporizes Rock!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
			elif computerAction == 'paper':
				print(Style.RED + 'Paper disaproves Spock!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1
			elif computerAction == 'scissors':
				print(Style.GREEN + 'Spock smashes Scissors!' + Style.RESET)
				playerScores.gamesWon = playerScores.gamesWon + 1
				computerScores.gamesLost = computerScores.gamesLost + 1
			else:
				print(Style.RED + 'Lizard poisons Spock!' + Style.RESET)
				playerScores.gamesLost = playerScores.gamesLost + 1
				computerScores.gamesWon = computerScores.gamesWon + 1

		currentScores()



def currentScores():
	print(Style.YELLOW + 'Current Scores \n' + Style.RESET)

	print('Player Scores')
	playerScores.stats()

	print('Computer Scores')
	computerScores.stats()

	input('Press Enter to Continue...')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
