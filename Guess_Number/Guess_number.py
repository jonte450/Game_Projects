import random
import sys

first = sys.argv[1]
last = sys.argv[2]

def random_number(num1,num2):
	return random.randint(num1,num2)

def check_first_last(num1,num2):
	if first.isdigit() == True and last.isdigit() == True:
		return first < last


def check_number(secret_number):
			count_guesses = 0
			while True:
				guess_number = input('Guess a number please! ')
				if not(guess_number.isnumeric()):
					while not guess_number.isnumeric():
						guess_number = input('Please enter an valid number and not letters! ')
				if int(guess_number) != secret_number:
					count_guesses += 1
					print(f'The {guess_number} is wrong!')
					print(f'Please try again and you guessed {count_guesses}!')
				elif int(guess_number) == secret_number:
					print(f'Congratulations you are right and you guessed {count_guesses}!')
					print(f'The number {guess_number} is the same as the secret number: {secret_number}')
					break
	
if first.isdigit() == True and last.isdigit() == True:
	if first < last:
		secret_number = random_number(int(first),int(last))
		check_number(secret_number)

while True:
	check_answer = input('Do you want to continue press c or do you want to quit press q: ')
	if check_answer == 'c':
		first = input('Enter first number: ')
		last = input('Enter second number: ')

		if check_first_last(first,last):
			secret_number = random_number(int(first),int(last))
			check_number(secret_number)
		else:
			while not(check_first_last(first,last)):
				first = input('Please enter a valid first number: ')
				last = input('Please enter a valid second number: ')
			secret_number = random_number(int(first),int(last))
			check_number(secret_number)

	if check_answer == 'q':
		print('The game quits')
		break	