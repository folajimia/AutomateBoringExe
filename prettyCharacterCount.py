
import pprint

message='It was a bright cold day in August and the clocks were striking thirteen.'
count={}


for character in message:
	count.setdefault(character, 0)
	count[character] =count[character] + 1

pprint.pprint(count)

""" if you want prettified as strings, you can use
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))"""