#Comma Code
#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns 
#a string with all the items separated by a comma and a space, with and 
#inserted before the last item. For example, passing the previous spam list to 
#the function would return 'apples, bananas, tofu, and cats'. But your func-
#tion should be able to work with any list value passed to it.

def tre(spam):
	newList=[]
	count = 0	
	for fruit in spam:
		count = count + 1
		if count == len(spam):
			newList.append(fruit)
		else:
			newList.append(fruit +',')
	newStr=''.join(newList)
	return newStr
		#print(fruit+',')
		#count=count+1
		#if count < len(spam)
		#	spamspam[count],

		#	spam.append('tour')

spam = ['apples', 'bananas', 'tofu', 'cats', 'roaches']


talk=tre(spam)
print talk