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

game = ''

playerScores = Scores(0, 0, 0)
computerScores = Scores(0, 0, 0)
classicChoices = ['rock', 'paper', 'scissors']
bigBangChoices = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def main():
        #Select Game Version to Play
	gameVersion = 0
	while gameVersion != 1 or gameVersion != 2:
		gameVersion = int(input('1: Classic Rock, Paper, Scissors \n' \
			'2: Rock, Paper, Scissors, Lizard, Spock \n' \
			'Selection: '))

		if gameVersion == 1:
			game = 'Classic'
			classicGame()
			break
		elif gameVersion == 2:
			game = 'BigBang'
			bigBang()
			break
		else:
			clearConsole()
			print('Please Enter a Valid Selection')
			main()
	endGame()


def classicGame():
        #Setup Classic
	clearConsole()

	print(f'{Style.YELLOW}Rock Paper Scirrors{Style.RESET}')
	print(f'{Style.BLUE}\nRULES{Style.RESET}')
	rules('Classic')
	totalGames = int(input('How Many Games to Play?: '))
	input('Press Enter to Continue...')
	playGame('Classic', classicChoices, totalGames)

def bigBang():
        #Setup BigBang
	clearConsole()

	print(f'{Style.YELLOW}Big Bang{Style.RESET}')
	print(f'{Style.BLUE}\nRULES{Style.RESET}')
	rules('BigBang')
	totalGames = int(input('How Many Games to Play?: '))
	input('Press Enter to Continue...')
	playGame('BigBang', bigBangChoices, totalGames)

def playGame(gameType, choices, totalGames):
        clearConsole()

	#Play Classic
        if gameType == 'Classic':
                gameCalculations(choices, totalGames)

	#Play BigBangTheory Version
        if gameType == 'BigBang':
                gameCalculations(choices, totalGames)


def endGame():
	clearConsole()
	userTotalWins = playerScores.getGamesWon()
	computerTotalWins = computerScores.getGamesWon()

	#If User Wins Display They Have Won
	if userTotalWins > computerTotalWins:
		print(f'{Style.GREEN}You Have Won!{Style.RESET}')
	#If Computer Wins, Display User Has Lost
	if computerTotalWins > userTotalWins:
		print(f'{Style.RED}You Have Lost!{Style.RESET}')
	#If Tied
	if userTotalWins == computerTotalWins:
		print(f'{Style.YELLOW}Game is a Tie{Style.RESET}')

	currentScores()

def rules(gameType):
	#Define Rules for Game Types
	if gameType == 'Classic':
		print(f'{Style.GREEN}Rock{Style.RESET} beats {Style.RED}Scissors{Style.RESET} \n' \
			+ f'{Style.GREEN}Paper{Style.RESET} beats {Style.RED}Rock{Style.RESET} \n' \
			+ f'{Style.GREEN}Scissors{Style.RESET} beats {Style.RED}Paper{Style.RESET} \n\n')
		print(f'To make a move, type in \'rock, paper or scissors\' in all {Style.underLine}lowercase{Style.RESET}')
	if gameType == 'BigBang':
		print(f'{Style.GREEN}Scissors{Style.RESET} cuts {Style.RED}Paper{Style.RESET} \n' \
			+ f'{Style.GREEN}Paper{Style.RESET} covers {Style.RED}Rock{Style.RESET} \n' \
			+ f'{Style.GREEN}Rock{Style.RESET} crushes {Style.RED}Lizard{Style.RESET} \n' \
			+ f'{Style.GREEN}Lizard{Style.RESET} poisons {Style.RED}Spock{Style.RESET} \n' \
			+ f'{Style.GREEN}Spock{Style.RESET} smashes {Style.RED}Scissors{Style.RESET} \n' \
			+ f'{Style.GREEN}Scissors{Style.RESET} decapites {Style.RED}Lizard{Style.RESET} \n' \
			+ f'{Style.GREEN}Lizard{Style.RESET} eats {Style.RED}Paper{Style.RESET} \n' \
			+ f'{Style.GREEN}Paper{Style.RESET} disaproves {Style.RED}Spock{Style.RESET} \n' \
			+ f'{Style.GREEN}Spock{Style.RESET} vaporizes {Style.RED}Rock{Style.RESET} \n' \
			+ f'And as it always has \n' \
			+ f'{Style.GREEN}Rock{Style.RESET} crushes {Style.RED}Scissors{Style.RESET} \n\n')
		print(f'To make a move, type in \'rock, paper scissors, lizard or spock\' in all {Style.underLine}lowercase{Style.RESET}')



def gameCalculations(choices, totalGames):
	for gameNumber in range(1, totalGames + 1, 1):
		clearConsole()

		print(f'Playing Game {gameNumber} of {totalGames}')

		userAction = input('Please Enter Your Move: ')
		computerAction = random.choice(choices)

		clearConsole()

		#Displays what User and Computers actions are
		print(f'User: {userAction}')
		print(f'Computer: {computerAction}')


		#Logic to disply Users action against Computer and what the outcome is
		#Updates Wins, Losses and Ties for each game outcome that is played
		if userAction == computerAction:
			print(f'{Style.YELLOW}It\'s a Tie{Style.RESET}')
			playerScores.gameTied()
			computerScores.gameTied()
		elif userAction == 'rock':
			if computerAction == 'paper':
				print(f'{Style.RED}Paper covers Rock!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(f'{Style.GREEN}Rock smashes Scissors!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'lizard':
				print(f'{Style.GREEN}Rock crushes Lizard!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(f'{Style.RED}Spock vaporizes Rock!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
		elif userAction == 'paper':
			if computerAction == 'rock':
				print(f'{Style.GREEN}Paper covers Rock!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'scissors':
				print(f'{Style.RED}Scissors cuts Paper!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'lizard':
				print(f'{Style.RED}Lizard eats Paper!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			else:
				print(f'{Style.GREEN}Paper disaproves Spock!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
		elif userAction == 'scissors':
			if computerAction == 'rock':
				print(f'{Style.RED}Rock smashes Scissors!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'paper':
				print(f'{Style.GREEN}Scissors cuts Paper!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'lizard':
				print(f'{Style.GREEN}Scissors decapitates Lizard!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(f'{Style.RED}Spock smashes Scissors!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
		elif userAction == 'lizard':
			if computerAction == 'rock':
				print(f'{Style.RED}Rock crushes Lizard{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'paper':
				print(f'{Style.RED}Lizard  eats Paper!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(f'{Style.RED}Scissors decapitates Lizard!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			else:
				print(f'{Style.GREEN}Lizard poisons Spock!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
		elif userAction == 'spock':
			if computerAction == 'rock':
				print(f'{Style.GREEN}Spock vaporizes Rock!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			elif computerAction == 'paper':
				print(f'{Style.RED}Paper disaproves Spock!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()
			elif computerAction == 'scissors':
				print(f'{Style.GREEN}Spock smashes Scissors!{Style.RESET}')
				playerScores.gameWon()
				computerScores.gameLost()
			else:
				print(f'{Style.RED}Lizard poisons Spock!{Style.RESET}')
				playerScores.gameLost()
				computerScores.gameWon()

		input()


def currentScores():
	print(f'{Style.YELLOW}Player Scores\t\t\tComputer Scores{Style.RESET}')
	print(f'Games Won: {Style.GREEN}{str(playerScores.getGamesWon())}{Style.RESET} \t\t\tGames Won: {Style.GREEN}{str(computerScores.getGamesWon())}{Style.RESET}')
	print(f'Games Lost: {Style.RED}{str(playerScores.getGamesLost())}{Style.RESET} \t\t\tGames Lost: {Style.RED}{str(computerScores.getGamesLost())}{Style.RESET}')
	print(f'Games Tied: {Style.YELLOW}{str(playerScores.getGamesTied())}{Style.RESET} \t\t\tGames Tied: {Style.YELLOW}{str(computerScores.getGamesTied())}{Style.RESET}')

	input('Press Enter to Exit...')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
