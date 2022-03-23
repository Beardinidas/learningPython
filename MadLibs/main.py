#!/usr/bin/python

import random
import os
import datetime

class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


letterFrom = 'Hello, my fellow {} in {}, it\'s me {},\n' \
		'the first {}. I am writting from the {}, where\n' \
		'I have been secretly living for the past {} years. I am\n' \
		'concerned by the {} state of affairs in {} these days.\n' \
		'Is seems that your politicians are more concerned with\n' \
		'{} one another than with listening to the\n' \
		'{} of the people. When we declared our independence\n' \
		'from the {}, we set fourth a/an {} path\n' \
		'guided by the voices of the everyday {}. If we\'re going to\n' \
		'keep {}, then we need ot learn how to respect all\n' \
		'{}. Don\'t get me wrong we had {} problems\n' \
		'in my day too. {} once called me a/an {}\n' \
		'and kicked me in the {}. But at the end of the day, we\n' \
		'were able to {} in harmony. Let us find that {}\n' \
		'spirit once again, or else I\'m taking my {} off the {}!'


def main():
	noun1 = input('Please Enter a Plural Noun: ')
	year = datetime.datetime.now().year
	name1 = input('Please Enter a Famous Person: ')
	occu = input('Please Enter an Occupation: ')
	place1 = input('Please Enter a Well Known Landmark: ')
	num = input('Please Enter a Number: ')
	adj1 = input('Please Enter an Adjective: ')
	country = input('Please Enter a Country: ')
	verb1 = input('Please Enter a Verb Ending in -ing: ')
	noun2 = input('Please Enter a Plural Noun: ')
	place2 = input('Please Enter a Well Known Landmark: ')
	adj2 = input('Please Enter an Adjective: ')
	noun3 = input('Please Enter a Plural Noun: ')
	verb2 = input('Please Enter a Verb Ending in -ing: ')
	noun4 = input('Please Enter a Plural Noun: ')
	adj3 = input('Please Enter an Adjective: ')
	name2 = input('Please Enter a Differnt Famous Person: ')
	noun5 = input('Please Enter a Noun: ')
	body1 = input('Please Enter a Body Part: ')
	verb3 = input('Please Enter a Verb: ')
	adj4 = input('Please Enter an Adjective: ')
	body2 = input('Please Enter a Body Part: ')
	currency = input('Please Enter A Currency [50p, pound, quarter, etc]: ')

	clearConsole()

	madLib = letterFrom.format(noun1,year,name1,occu,place1,num,adj1,country,verb1,noun2,place2,adj2,noun3,verb2,noun4,adj3,name2,noun5,body1,verb3,adj4,body2,currency)

	print(Style.YELLOW + 'MADLIBS' + Style.RESET)
	print(Style.GREEN + f'A Letter from {name1} ' + Style.RESET)

	print(madLib)

def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
