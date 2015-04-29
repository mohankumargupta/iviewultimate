from bs4 import BeautifulSoup
import requests

class IViewParser:
	def __init__(self, url):
		r = requests.get(url)
		self.soup = BeautifulSoup(r.text);

	def findAll(self, tag):
		return self.soup.find_all(tag) 

if __name__ == '__main__':
    parser = IViewParser('https://tviview.abc.net.au/iview/feed/sony/?keyword=0-Z')
    allvideos = parser.findAll('asset')
    for i in range(2):
    	print(allvideos[i])
   
