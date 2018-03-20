import bs4 as bs
import urllib.request
import sys

url = sys.argv[1]
content = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(content)
for link in soup.find_all('a'):
    print(link.get('href'))
