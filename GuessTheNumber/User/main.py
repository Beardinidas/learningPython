#!/usr/bin/python

import random
import os

randomMin = 1
randomMax = 1000

userGuesses = []

def main():
	#Generate a Random Interger
	randomNumber = random.randint(randomMin, randomMax)

	#Initialise userGuess to 0
	userGuess = 0
	lastGuess = 'No Guesses have been Made'

	#Loop Until Correct Guess
	while userGuess != randomNumber:
		clearConsole()

		print(f"Your Last Guess Was: {lastGuess}")
		print(f"Guesses Made: {userGuesses}")
		userGuess = int(input("Guess a Number: "))

		"Add User's Guess to Array"
		userGuesses.append(userGuess)

		"If Guess Lower than randomNumber"
		if userGuess < randomNumber:
			print("Too Low")
			lastGuess = "Too Low"
		"If Guess Higher Than randomNumber"
		if userGuess > randomNumber:
			print("Too High")
			lastGuess = "Too High"

	#If Correct Guess is Made
	clearConsole()
	print(f"You Have Guessed the Correct Number: {randomNumber} in {len(userGuesses)} Guesses")



def clearConsole():
	os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
	main()
