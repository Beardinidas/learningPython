#!/usr/bin/python

import random
import os
import string


characters = list(string.ascii_letters + string.digits + string.punctuation)


class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


def main():
	clearConsole()
	print(f'{Style.GREEN}Password Generator{Style.RESET}')

	print(f'Min Password Length is 8 characters')
	#Get Password Length entered Else Default to 8
	passwordLength = int(input(f'If you want a longer password \n' \
		+ 'Enter Length here or hit Enter for Default: ') or 8)

	#If Password Length is 7 or less defalt password length to 8 
	#Else use password Length Entered
	if passwordLength <= 7:
		passwordLength = 8
	else:
		passwordLength = passwordLength

	password = generatePassword(passwordLength)

	print(f'{password}')


def generatePassword(passwordLength):
	#Shuffle Characters
	random.shuffle(characters)

	password = []
	#Generate a Password of Length
	for char in range(passwordLength):
		password.append(random.choice(characters))

	password = ''.join(password)
	return password

def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
