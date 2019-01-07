import requests
from bs4 import BeautifulSoup

class Google:
	@staticmethod
	def search(term, n):
		url = "https://www.google.com/search?q={0}".format(term)
		request = requests.get(url)
		soup = BeautifulSoup(request.text, 'html5lib')
		headlines = soup.find_all('h3', class_='r')
		results = []
		if(n > 9):
			n = 9
		for i in range(0,n+1):
			links = headlines[i].a.get('href')
			a = links.split('&')
			if a[0].replace("/url?q=","") != "/search?q=" + term:
				results.append(a[0].replace("/url?q=",""))
		return results
