#!/usr/bin/python

import os


class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


files = './files/'

def main():
	print(f'{Style.GREEN}BULK FILE RENAMER{Style.RESET}\n')
	print(f'{Style.RED}Please Ensure Files are in the \'files\' Folder{Style.RESET}')
	input('Press Enter to Continue')

	clearConsole()

	capture = input(f'What has been captured?: ').strip()

	fileCounter = 0

	#Change Directory to Files Folder
	os.chdir(files)

	print('Renaming Files...')
	for file in os.listdir():
		fileName, fileExt = os.path.splitext(file)

		#Reassign fileName to Capture
		#zfill will pad counter to 3 digits
		fileName = f'{capture}_{str(fileCounter).zfill(3)}'

		#New FileName with Original Extension
		newFileName = f'{fileName}{fileExt}'

		#Rename File
		os.rename(file, newFileName)

		fileCounter += 1


	print(f'{Style.GREEN}Renaming Complete!{Style.RESET}')

def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
