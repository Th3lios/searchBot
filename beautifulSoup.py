from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print (e)
try:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    title = bsObj.body.h1
except AttributeError as e:
    print (e)

print (title)
