#!/usr/bin/python

import random
import os


class Style():
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'


class Scores():
	gamesWon = 0
	gamesLost = 0
	gamesTied = 0

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
	print(Style.YELLOW + 'Rock Paper Scirros' + Style.RESET)
	rules('Classic')
	input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
	clearConsole()

	print(Style.YELLOW + 'Rock Paper Scissors' + Style.RESET)
	totalGames = int(input('How Many Games to Play?: '))
	playGame('Classic', totalGames)


def bigBang():
	#Setup BigBang
	clearConsole()
	print(Style.YELLOW + 'Big Bang' + Style.RESET)
	rules('BigBang')
	input(Style.BLUE + 'Press Enter to Continue...' + Style.RESET)
	clearConsole()

	print(Style.YELLOW + 'Big Bang' + Style.RESET)
	totalGames = int(input('How Many Games to Play?: '))
	playGame('BigBang', totalGames)


def playGame(gameType, totalGames):
	#Play Game
	clearConsole()
	playerScores = Scores()
	computerScores = Scores()

	if gameType == 'Classic':
		print(f'Playing {totalGames} Games of {gameType} Rock Paper Scissors')
		input('Press Enter to Continue...')
		clearConsole()

		for game in range(1, totalGames + 1, 1):
			clearConsole()
			print(f'Playing Game {game} of {totalGames}')
			#TODO

	if gameType == 'BigBang':
		print(f'Playing {totalGames} Games of Sheldon\'s Rock Paper Scissors')
		input('Press Enter to Continue...')
		clearConsole()

		for game in rang(1, totalGames + 1, 1):
			clearConsole()
			print(f'Playing Game {game} of {totalGames}')
			#TODO


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
