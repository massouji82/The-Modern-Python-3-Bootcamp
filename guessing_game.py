from random import randint

print('*** Welcome to the Guessing Game ***\n')

def game():
	num = randint(1,100)
	tries = 0
	guess = None
	while guess != num:
		guess = int(input('Guess a number between 1 and 100: '))
		if num > guess:
			print('Your guess is too low!\n')
			tries += 1
		elif num < guess:
			print('Your guess is too high!\n')
			tries += 1
		elif num < 0 or num > 100:
			print('Your guess must be between 1 and 100!\n')
			tries += 1
		else:
			print(f'***Correct! The number is {num}***\nYou guessed {tries} times.\n')
			again()

def again():
	while True:
		answer = input('Do you want to play again? y/n ').lower()
		if answer == 'y':
			game()
		elif answer == 'n':
			print('Goodbye!\n')
			break
		else:
			print('Please type y or n\n')

print(game())

	
