import sys
number=0


def collatz(number):
	if (number % 2 == 0):
		return (number // 2)
	else:
		return (3 * number +1)

print('Enter a number')
number = int(input())
colNum = collatz(number)
while colNum!=1:
	colNum = collatz(colNum)
	#if (colNum ==1):
	#	sys.exit()


#if collatz(number)==1:
#	exit 0
#else:

#test=collatz(number)