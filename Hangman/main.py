#!/usr/bin/python

import random
import os
import base64
from PyDictionary import PyDictionary


class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'


HANGMAN = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===
''']


dict = PyDictionary()
wordlist = list()
correctGuesses = []
incorrectGuesses = []
currentGuessState = ''

def main():
	#Import List of Words
	loadListOfWords()

	#Get a Random Word from List
	secret = base64.b64decode(random.choice(wordlist)).decode('utf-8')

	#Start Game
	playGame(secret)

	#Get Definition of Word + Print
	definition = dict.meaning(secret)
	print(f'{secret} : {definition}')



def loadListOfWords():
	#Import List of Words
	with open('wordlist') as f:
		#Import Each Line 'Word' at a Time
		for line in f:
			wordlist.append(line.replace('\n', '') + '==')


def playGame(secret):
	#Split Secret Word into Characters
	charsInSecret = list(secret)

	life = 0
	while life < len(HANGMAN):
		print(Style.YELLOW + 'HANGMAN\n' + Style.RESET)
		#Get Input From Uses
		guess = input("Please Enter a Guess: ")

		if guess in correctGuesses:
			input('You Have Already Guessed {guess} which was ' + Style.GREEN + 'CORRECT!' + Style.RESET)
		elif guess in incorrectGuesses:
			input('You Have Already {guess} which was ' + Style.RED + 'INCORRECT!' + Style.RESET)
		else:
			if guess in charsInSecret:
				#IF CHARACTER IN SECRET
				correctGuesses.append(guess)
				input('You Have Guessed a Correct Letter!')
				getGuessState(guess)
			else:
				#IF CHARACTER NOT IN SECRET
				incorrectGuesses.append(guess)
				print(Style.RED + HANGMAN[life] + Style.RESET)
				input(f'Guess {guess} Is Not Correct')
				life += 1


def getGuessState(guess):
	#TODO Guess State displaying Current Corect Guesses in positions


def clearConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
        main()
