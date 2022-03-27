#!/usr/bin/python

import random
import os

class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


def main():
	print('TODO')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
