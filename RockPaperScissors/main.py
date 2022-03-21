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
	def __init__(self, gamesWon, gamesLost, gamesTied):
		self.gamesWon = gamesWon
		self.gamesLost = gamesLost
		self.gamesTied = gamesTied

	def gameWon(self):
		self.gamesWon += 1

	def gameLost(self):
		self.gamesLost += 1

	def gameTied(self):
		self.gamesTied += 1

	def getGamesWon(self):
		return self.gamesWon

	def getGamesLost(self):
		return self.gamesLost

	def getGamesTied(self):
		return self.gamesTied


playerScores = Scores(0, 0, 0)
computerScores = Scores(0, 0, 0)


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


	userTotalWins = playerScores.getGamesWon
	computerTotalWins = computerScores.getGamesWon

	if userTotalWins.getGamesWon > computerTotalWins.getGamesWon:
		print(Style.GREEN + 'You Have Won!' + Style.Reset)
	elif computerTotalWins.getGamesWon > userTotalWins.getGamesWon:
		print(Style.RED + 'You Have Lose!' + Style.Reset)
	else:
		print(Style.YELLOW + 'It\'s a Tie' + Style.Reset)


def classicGame():
        #Setup Classic
	clearConsole()

	#Choices tat are applicable
	choices = ['rock', 'paper', 'scissors']
	print(Style.YELLOW + 'Rock Paper Scirrors' + Style.RESET)
	print(Style.BLUE + '\nRULES' + Style.RESET)
	rules('Classic')
	totalGames = int(input('How Many Games to Play?: '))
	input('Press Enter to Continue...')
	playGame('Classic', choices, totalGames)

def bigBang():
        #Setup BigBang
	clearConsole()

	#Choices that are applicable 
	choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
	print(Style.YELLOW + 'Big Bang' + Style.RESET)
	print(Style.BLUE + '\nRULES' + Style.RESET)
	rules('BigBang')
	totalGames = int(input('How Many Games to Play?: '))
	input('Press Enter to Continue...')
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
                        + Style.GREEN + 'Scissors' + Style.RESET + ' beats ' + Style.RED + 'Paper \n\n' + Style.RESET)
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
                        + Style.GREEN + 'Rock' + Style.RESET + ' crushes ' + Style.RED + 'Scissors \n\n' + Style.RESET)


def gameCalculations(choices, totalGames):
	for game in range(1, totalGames + 1, 1):
		clearConsole()

		print(f'Playing Game {game} of {totalGames}')

		userAction = input('Please Enter Your Move: ')
		computerAction = random.choice(choices)

		clearConsole()

		print(f'User: {userAction}')
		print(f'Computer: {computerAction}')

		if userAction == computerAction:
			print('It is a Tie')
			playerScores.gameTied()
			computerScores.gameTied()
		elif userAction == 'rock':
			if computerAction == 'paper':
				print(Style.RED + 'Paper covers Rock!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(Style.GREEN + 'Rock smashes Scissors!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'lizard':
				print(Style.GREEN + 'Rock crushes Lizard!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(Style.RED + 'Spock vaporizes Rock!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
		elif userAction == 'paper':
			if computerAction == 'rock':
				print(Style.GREEN + 'Paper covers Rock!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'scissors':
				print(Style.RED + 'Scissors cuts Paper!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'lizard':
				print(Style.RED + 'Lizard eats Paper!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			else:
				print(Style.GREEN + 'Paper disaproves Spock!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
		elif userAction == 'scissors':
			if computerAction == 'rock':
				print(Style.RED + 'Rock smashes Scissors!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'paper':
				print(Style.GREEN + 'Scissors cuts Paper!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'lizard':
				print(Style.GREEN + 'Scissors decapitates Lizard!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(Style.RED + 'Spock smashes Scissors!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
		elif userAction == 'lizard':
			if computerAction == 'rock':
				print(Style.RED + 'Rock crushes Lizard' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'paper':
				print(Style.RED + 'Lizard  eats Paper!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(Style.RED + 'Scissors decapitates Lizard!' + Style.RESET)
				playerScores.GameLost()
				computerScores.gameWon()
			else:
				print(Style.GREEN + 'Lizard poisons Spock' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
		elif userAction == 'spock':
			if computerAction == 'rock':
				print(Style.GREEN + 'Spock vaporizes Rock!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'paper':
				print(Style.RED + 'Paper disaproves Spock!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(Style.GREEN + 'Spock smashes Scissors!' + Style.RESET)
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(Style.RED + 'Lizard poisons Spock!' + Style.RESET)
				playerScores.gameLost()
				computerScores.gameWon()

		currentScores()



def currentScores():
	input()
	print(Style.YELLOW + 'Player Scores' + Style.RESET)
	print('Games Won: ' + Style.GREEN + str(playerScores.getGamesWon()) + Style.RESET)
	print('Games Lost: ' + Style.RED + str(playerScores.getGamesLost()) + Style.RESET)
	print('Games Tied: ' + Style.YELLOW + str(playerScores.getGamesTied()) + Style.RESET)

	print(Style.YELLOW + 'Computer Scores' + Style.RESET)
	print('Games Won: ' + Style.GREEN + str(computerScores.getGamesWon()) + Style.RESET)
	print('Games Lost: ' + Style.RED + str(computerScores.getGamesLost()) + Style.RESET)
	print('Games Tied: ' + Style.YELLOW + str(computerScores.getGamesTied()) + Style.RESET)

	input('Press Enter to Continue...')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
