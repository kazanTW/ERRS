# Easy Record Register System(ERRS)
# Python 3
# Kazan 2021 

import getpass
import pandas as pd

def Registration():
	print()

def Login(login):
	if (login == usrName):
			login_pwd = getpass.getpass(f'Please enter your password: ')
			if (login_pwd == usrPwd):
				choice = input(f'Welcome {usrName}! What do you want to do?')
			else:
				wrongCounter = 1
				login_pwd = getpass.getpass(f'Wrong password, please try again: ')
				while (wrongCounter != 5):
					if (login_pwd != usrPwd):
						wrongCounter += 1
						login_pwd = getpass.getpass(f'Wrong password, please try again: ')
					else:
						break
				if (wrongCounter == 5):
					print(f'You have entered wrong password for 5 times. You will be kicked out, and please try login again.')
				elif (wrongCounter != 5):
					choice = input(f'Welcome {usrName}! What do you want to do?')
				

if __name__ == '__main__':
	print(f'Easy Record Register System (beta v1.0)')
	print(f'Copyright © 2021 Kazan All Rights Reserved.')
	print()

	usrName = pd.read_excel()
	usrPwd = pd.read_excel()
	
	# Login phase, or new user register.
	login = input(f'Please enter your username (Enter "R" for new user registration): ')
	if (login == "R"):
		Registration()
	else:
		Login(login)

	