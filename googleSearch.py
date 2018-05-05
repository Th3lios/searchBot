#! /usr/bin/python
from bs4 import BeautifulSoup
from collections import Counter
import requests
cont = 0
cont2 = 0
cont3 = 0
searchResult = []
query = input("consulta en google: ")
key = input("Ingresa palabra clave: ")
key2 = input("Ingresa palabra clave: ")
key3 = input("Ingresa palabra clave: ")

i=0
print(query)
search = query.replace(" ","+")
googleSearch = "https://www.google.cl/search?q="+search+" "+key+" "+key2+" "+key3
r = requests.get(googleSearch)
soup = BeautifulSoup(r.text,"html.parser")
url  = soup.findAll('span',{"class":"st"})
for i in url:
    value = i.get_text()
    print(value)
    if(key in value):
        cont += 1
    if(key2 in value):
        cont2 += 1
    if(key3 in value):
        cont3 += 1
contf = cont+cont2+cont3
if contf == 0:
    contf = 1
print(str(cont / contf * 100)+"% - "+key)
print(str(cont2 / contf * 100)+"% - "+key2)
print(str(cont3 / contf * 100)+"% - "+key3)
