'''
MAIN GOAL
Create a program that allows the user to 
input the sides of any triangle, 
and then return whether the triangle is a 
Pythagorean Triple or not.

SUBGOALS
*If your program requires users to input 
the sides in a specific order, 
change the coding so the user can type in
the sides in any order. Remember, 
the hypotenuse (c) is always the longest side.

*Loop the program so the user can use it more 
than once without having to restart the program.'''


def pyt():
	try:
		sideA = int(input('Input three sides of a triangle, hit enter after each side\nA: '))
		sideB = int(input('B: '))
		sideC = int(input('C: '))
		if sideA + sideB == sideC or sideA + sideC == sideB or sideB + sideC == sideA:
			print('Your triangle is a Pythagorean triangle!')
		else:
			print('Your triangle is not a Pythagorean triangle!')
	except ValueError:
		print('Input is not a number. It\'s a string')
		pyt()
	again()

def again():
	x = input('Do you want to continue? yes/no\n')
	if x.lower() == 'yes':
		pyt()
	elif x.lower() == 'no':
		print('Goodbye!')
		quit()
	else:
		print('Please type Yes or No')
	again()

print(pyt())


	



