#Guess the number

from random import randint

print('***WELCOME TO GUESS THE NUMBER!***')
random_num = randint(1,10)
guess = None

while guess != random_num:
	guess = int(input('Guess a number between 1 and 10: '))
	if guess > random_num and guess < 11:
		print('Your guess is too high!')
	elif guess < random_num and guess > 0:
		print('Your guess is too low!')
	elif guess > 10 or guess < 0:
		print('Your guess must be between 1 and 10!')
	else:
		print(f'Correct! the number was {random_num}!')

# random_number = random.randint(1,10)

# guess = None

# while guess != random_number:
# 	guess = input ('Pick a number from 1 to 10: ')
# 	guess = int(guess)
# 	if guess < random_number:
# 		print ('Too low!')
# 	elif guess > random_number:
# 		print ('Too high!')
# 	else:
# 		print (f'Correct! the number was {random_number}!')





