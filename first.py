import requests
from bs4 import BeautifulSoup
url='http://www.pythonscraping.com/pages/page1.html'
req=requests.get(url)
# print(req.text)
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.h1)