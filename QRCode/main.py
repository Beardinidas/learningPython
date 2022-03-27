##!/usr/bin/python

import random
import os
import qrcode
import time


class Style:
	RESET = '\033[0m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	underLine = '\033[4m'


def main():
	ed = ''
	while ed != 'E' or ed != 'D':
		clearConsole()
		print(f'E: Encode')
		print(f'D: Decode')
		ed = input('Selection: ').upper()

		if ed == 'E':
			qrEncode()
			print('Encoding Data Complete!')
			break
		if ed == 'D':
			qrDecode()
			print('Decoding QRCodes Complete!')
			break



def qrEncode():
	print('ENCODE')

	end = ''
	while end != 'exit!':
		clearConsole()
		#Ensures Unique File Name
		uts = int(time.time())
		data = input('What do you want to Encode into a QR Code?: ')
		#Data to Encode into a QR Code Saved into qrCodeImg
		qrCodeImg = qrcode.make(data)
		type(qrCodeImg)
		#Save the QRCode into the encode Folder
		qrCodeImg.save(f'./qrs/encode/qrCode_{uts}.png')

		#Write QRCode Image file name and Data Encoded to txt file in Encode Folder
		#This will Create the qrCodeData File if it Does Not Exist and Append Data to the end
		with open('./qrs/encode/qrCodeData.txt', 'a') as f:
			f.write(f'qrCode_{uts}: {data}\n')

		clearConsole()
		end = input(f'To Encode More Data Hit Enter else type {Style.RED}exit!{Style.RESET}: ').lower()


def qrDecode():
	clearConsole()
	print('DECODE')
	print(f'{Style.RED}Please Ensure your QR Data Files are In the Correct Folder!{Style.RESET}')
	print(f'Note only {Style.GREEN}.png{Style.RESET} are supported')
	input('Press Enter to Continue')

	print('TODO')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
