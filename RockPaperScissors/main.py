#!/usr/bin/python

import random
import os


totalGames = 0
totalGamesPlayed = 0
userWins = 0
computerWins = 0


class Style():
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'


def main():
	#Select Game Version to Play
	gameVersion = 0
	while gameVersion != 1 or gameVersion != 2:
		gameVersion = int(input('1: Classic Rock, Paper, Scissors \n' \
			'2: Rock, Paper, Scissors, Lizard, Spock \n' \
			'Selection: '))

		if gameVersion == 1:
			classicGame()
		elif gameVersion == 2:
			bigBang()
		else:
			clearConsole()
			print('Please Enter a Valid Selection')
			main()


def classicGame():
	#Logic for Classic RPS
	clearConsole()
	print(Style.YELLOW + 'Rock Paper Scirros' + Style.RESET)
	rules('Classic')
	input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
	clearConsole()


def bigBang():
	#Logic for BigBang
	clearConsole()
	print(Style.YELLOW + 'Big Bang' + Style.RESET)
	rules('BigBang')
	input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
	clearConsole()



def playGame(gameType):
	return 0



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


def clearConsole():
	os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
	main()
