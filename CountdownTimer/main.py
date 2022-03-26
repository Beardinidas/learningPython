#!/usr/bin/python

import random
import os
import time

class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


def main():
	hours = input('Enter Hours: ')
	mins = input('Enter Minutes: ')
	seconds = input('Enter Seconds: ')

	#Convert Total Time into Seconds
	hoursInSeconds = int(hours) * 3600
	minsInSeconds = int(mins) * 60
	totalTime = int(hoursInSeconds) + int(minsInSeconds) + int(seconds)

	clearConsole()
	input(f'{Style.GREEN}Hit Enter To Start Timer{Style.RESET}')

	countDown(totalTime)

	print(f'{Style.RED}TIMES UP!{Style.RESET}')

def countDown(totalTime):
	while totalTime > 0:
		if totalTime > 10:
			print(f'{Style.GREEN}{str(totalTime)}{Style.RESET}')
			totalTime -= 1
			time.sleep(1)
		if totalTime <=10 and totalTime > 0:
			print(f'{Style.RED}{str(totalTime)}{Style.RESET}')
			totalTime -= 1
			time.sleep(1)

def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
