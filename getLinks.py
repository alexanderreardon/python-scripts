# Originally developed for Bryant REDDay 2018 Presentation
import bs4, sys
from urllib.request import urlopen

def getLinks(url):
	# Adds HTTP protocol if not specified in user input:
	if (url.startswith('http://') or url.startswith('https://')):
		url = url
	else:
		url = 'http://' + url

	source = urlopen(url).read()
	soup = bs4.BeautifulSoup(source, 'lxml')
	links = soup.find_all('a')
	for a in links:
		print(a.get('href'))

# If URL is specified from command line, use that. Otherwise, ask the user:
if len(sys.argv) == 1:
	getLinks(input("Enter the web address: "))
elif len(sys.argv) == 2:
	getLinks(sys.argv[1])

# Prevents window from closing automatically if not run from Command Line:
input("[ Press any key to close. ]")