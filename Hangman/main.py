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
	currentWord = ''

	while life < len(HANGMAN) and currentWord != secret:
		clearConsole()
		print(f'{Style.YELLOW}HANGMAN{Style.RESET}')
		print(f'{Style.RED}{currentHangState}{Style.RESET}')

		#Prints Current State of Secret with Correctly Guessed Charactes and Blanks
		getGuessState(secret)

		print(f'{Style.GREEN}{str(correctGuesses)}{Style.RESET}')
		print(f'{Style.RED}{str(incorrectGuesses)}{Style.RESET}')


		#Get Input From Uses
		guess = input("Please Enter a Guess: ")

		if guess in correctGuesses:
			getGuessState(secret)
			input(f'You Have Already Guessed {guess} which was {Style.GREEN}CORRECT!{Style.RESET}')
		elif guess in incorrectGuesses:
			getGuessState(secret)
			input(f'You Have Already {guess} which was {Style.RED}INCORRECT!{Style.RESET}')
		else:
			if guess in charsInSecret:
				#If Guess Appears In Secret
				correctGuesses.append(guess)
				input(f'{Style.GREEN}You Have Guessed a CORRECT Letter!{Style.RESET}')
			else:
				#Ic Guess Does Not Appear In Secret
				incorrectGuesses.append(guess)
				input(f'{Style.RED}Sorry, {guess} is INCORRECT!{Style.RESET}')
				currentHangState = HANGMAN[life]
				life += 1
		#Updates Current Word to Check If Guess is Correct
		currentWord = getGuessState(secret)


	#If User Has No Lives 
	if life == 7:
		clearConsole()
		print(Style.RED + HANGMAN[6] + Style.RESET)
		endGame('life', secret)
	#If User Has Guesed The Word Correctly
	if currentWord == secret:
		clearConsole()
		print(Style.RED + currentHangState + Style.RESET)
		endGame('win', secret)



def getGuessState(secret):
	#Replaces Occurance of Correct Character In secret Ensuring to Cover Duplicates
	currentWordList = [char if char in correctGuesses else '_' for char in secret]
	#Converts the List of Correct Guesses in secret into a string
	currentWord = ''.join(currentWordList)
	print(currentWord)

	return currentWord


def getDefinition(secret):
	#Gets the Definition of Secret
	definition = dict.meaning(secret)
	print(f'{secret}: {definition}')



def endGame(endType, secret):
	if endType == 'life':
		print(f'Sorry You Have Not Managed to Guess The Word. \nThe Word was: {secret}')
		getDefinition(secret)
	if endType == 'win':
		print(f'Congrats! You Have Guessed the Word {secret} Correctly!')
		getDefinition(secret)


def clearConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
        main()
