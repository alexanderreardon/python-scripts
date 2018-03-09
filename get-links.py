from bs4 import BeautifulSoup
import urllib
import sys

url = sys.argv[1]
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content)
for link in soup.find_all('a'):
    print(link.get('href'))
