# allow user to input how many coins they have (pennies, nickels, dimes, quarters)
# how many wrappers? how many coins? total value?
import math


try:
	p = int(input('How many grams pennies do you have? \n'))
	n = int(input('How many grams nickels do you have? \n'))
	d = int(input('How many grams dimes do you have? \n'))	
	q = int(input('How many grams quarters do you have? \n'))

except ValueError:
	print('Input is not a number. It\'s a string')
	p = int(input('How many grams pennies do you have? \n'))
	n = int(input('How many grams nickels do you have? \n'))
	d = int(input('How many grams dimes do you have? \n'))	
	q = int(input('How many grams quarters do you have? \n'))
	
pen_w = math.ceil((p/2.5)/50)
nic_w = math.ceil((n/5)/40)
dim_w = math.ceil((d/2.268)/50)
qua_w = math.ceil((q/5.67)/40)

pen = round(p/25)
nic = round(n/5)
dim = round(d/2.268)
qua = round(q/5.67)

pen_dol = round(pen/100, 1)
nic_dol = round(nic/20, 1)
dim_dol = round(dim/10, 1)
qua_dol = round(qua/4, 1)

total = pen_dol+nic_dol+dim_dol+qua_dol

print(f'You have {pen} pennies, {nic} nickels, {dim} dimes and {qua} quarters.')
print(f'You need {pen_w} penny wrapper(s), {nic_w} nickel wrapper(s), {dim_w} dime wrapper(s) and {qua_w} quarter wrapper(s).')
print(f'The estimated total value of your coins are {total} dollars.')




# penny = 2.5 grams  	50 per roll
# nickel = 5 grams		40 per roll
# dime = 2.268 grams	50 per roll
# quarter = 5.67 grams	40 per roll


