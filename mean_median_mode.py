def mean(numlist):
	theSum = 0
	for i in numlist:
		theSum += i
	return sum(numlist)/len(numlist)

def mode(numlist):
	for i in numlist:
		return max(numlist)

numlist = [2,4,6,8,10,10,8,8]

print(mean(numlist))
print(mode(numlist))