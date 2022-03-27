#!/usr/bin/python

import random
import os
import qrcode
from datetime import datetime

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



def qrEncode():
	print('ENCODE')

	end = ''
	counter = 0
	date = datetime.today().strftime('%Y%m%d')
	print(date)
	while end != 'exit!':
		clearConsole()
		data = input('What do you want to Encode into a QR Code?: ')
		#Data to Encode into a QR Code Saved into qrCodeImg
		qrCodeImg = qrcode.make(data)
		type(qrCodeImg)
		#Save the QRCode into the encode Folder
		qrCodeImg.save(f'./qrs/encode/qrCode_{date}_{counter}.png')

		#Write QRCode Image file name and Data Encoded to txt file in Encode Folder
		with open('./qrs/encode/qrCodeData.txt', 'a') as f:
			f.write(f'qrCode_{date}_{counter}: {data}\n')

		clearConsole()
		end = input(f'To Encode More Data Hit Enter else type {Style.RED}exit!{Style.RESET}: ').lower()
		counter += 1


def qrDecode():
	print('DECODE')
	print(f'{Style.RED}Please Ensure your QR Data Files are In the Correct Folder!{Style.RESET}')
	input('Press Enter to Continue')

	print('TODO')


def clearConsole():
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
        main()
