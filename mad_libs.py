
'''Create a Mad Libs style game, 
where the program asks the user for certain types of words, 
and then prints out a story with the words that the user inputted. 
The story doesn't have to be too long, 
but it should have some sort of story line.'''

na = input('Enter a name\n ').capitalize()
ad = input('Enter an adverb\n ')
no = input('Enter a noun\n ')
adj = input('Enter an adjective\n ')
no1 = input('Enter another noun\n ')

vowels = ["a","e","i","o","u"]

if no1[0].lower() in vowels: 
	print(f"My name is {na} she yelled {ad}, as she jumped into her convertible {no} and drove off with her {adj} wife and an {no1}")
else:
	print(f"My name is {na} she yelled {ad}, as she jumped into her convertible {no} and drove off with her {adj} wife and a {no1}")




