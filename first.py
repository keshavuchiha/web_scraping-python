# import requests
from email.policy import HTTP
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='http://www.pythonscraping.com/pages/page1.html'
req=urlopen(url)
# print(req.text)
try:
    bs = BeautifulSoup(req.read(), 'lxml')
except HTTPError as e:
    print(e)
except URLError as e:
    print('the server not found')
else:
    print(bs.h1)