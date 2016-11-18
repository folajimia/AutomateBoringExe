def collatz(number):
	if (number % 2) == 0:
		print(number//2)
	else:
		print(str(3*number+1))




test=0


if  test != 1:
	print('Enter a number')
	number=int(input())
	test=collatz(number)
else:
	print ("Great you found a collatz number" + number)

#if (str(test) == 1):
#	print ("Great you found a collatz number" + test)
	

#while (str(test) != 1):
#	print ("Try again")
#	collatz(number)
