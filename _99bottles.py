for n in range(99,0,-1):
	if n >= 2 and n <=99:
		print(f'{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n')
	else:
		print(f'{n} bottle of beer on the wall, {n} bottle of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n')
n=99
print(f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {n} bottles of beer on the wall.\n')


