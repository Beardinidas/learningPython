#!/usr/bin/python

import random
import os

computerGuesses = []

#Start and End Underline
underLineS = "\033[4m"
underLineE = "\033[0m"

def main():
	randomMin = 1
	randomMax = 1000
	guessFeedback = ''

	print(f"Pick a Number Between {randomMin} and {randomMax} to Guess")
	input("Press Enter to Continue...")

	guess = random.randint(randomMin, randomMax)

	"Loop Until Correct Guess"
	while guessFeedback != 'C':
		if randomMin != randomMax:
			guess = random.randint(randomMin, randomMax)
		else:
			guess = randomMax #This can also be randomMin as it is the same as randomMax 

		clearConsole()

		#Change input to Uppercase to ensure 
		guessFeedback = input(f'Is {guess} too {underLineS}H{underLineE}igh, ' \
			f'too {underLineS}L{underLineE}ow ' \
			f'or {underLineS}C{underLineE}orrect?: ').upper()

		#Alter Min, Max Values Depending if Guess is Too Low or Too High
		if guessFeedback == 'H':
			randomMax = guess-1
			computerGuesses.append(guess)
		elif guessFeedback == "L":
			randomMin = guess+1
			computerGuesses.append(guess)

	print(f"Computer Has Guessed Your Number, {guess} Correctly in {len(computerGuesses)} Guesses")


def clearConsole():
	os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
	main()
