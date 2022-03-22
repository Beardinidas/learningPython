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
currentWord = ''

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
	currentHangState = ''

	while life < len(HANGMAN):
		clearConsole()
		print(Style.YELLOW + 'HANGMAN' + Style.RESET)
		print(Style.RED + currentHangState + Style.RESET)
		print(Style.GREEN + str(correctGuesses) + Style.RESET)
		print(Style.RED + str(incorrectGuesses) + Style.RESET)

		#Get Input From Uses
		getGuessState(True, secret)
		guess = input("Please Enter a Guess: ")

		if guess in correctGuesses:
			input('You Have Already Guessed {guess} which was ' + Style.GREEN + 'CORRECT!' + Style.RESET)
		elif guess in incorrectGuesses:
			input('You Have Already {guess} which was ' + Style.RED + 'INCORRECT!' + Style.RESET)
		else:
			if guess in charsInSecret:
				#IF CHARACTER IN SECRET
				correctGuesses.append(guess)
				input(Style.GREEN + 'You Have Guessed a CORRECT Letter!' + Style.RESET)
				getGuessState(False, secret)
			else:
				#IF CHARACTER NOT IN SECRET
				incorrectGuesses.append(guess)
				input(Style.RED + f'Sorry, {guess} is INCORRECT' + Style.RESET)
				currentHangState = HANGMAN[life]
				life += 1


def getGuessState(isFirstGuess, secret):
	secretLength = len(secret)
	displayBlanks = '_' * secretLength

	if isFirstGuess == True:
		#Print _ Based on Charactes in Word
		print(displayBlanks)
	else:
		#PRINT CORRECT GUESS IN WORD IN CORRECT PLACE
		print('TEST')



def clearConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
        main()
