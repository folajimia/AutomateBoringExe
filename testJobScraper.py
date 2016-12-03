
#!
#The script should be able to search job index for text positions and list them
#i will start with google search and modify

import requests, sys, webbrowser, bs4

print('Googling.....') #display text while downloading google text
res = requests.get ('http://google.com/search?q=' + ''.join(sys.argv[1:])+'&tbs=qdr:w')  # append  ('&tbs=qdr:w') to search for available results in the past 1 week. replace w with m for month 
res.raise_for_status()

#print res

# retrieve top search results links.
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select('.r a')

#open a browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))