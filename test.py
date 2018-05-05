#! /usr/bin/python
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

string2 = []
f = open("/Users/macbook/Desktop/Elias/SearchBot/text/texto","r")
string = f.read()
print(string)
print(string.split("\n\n"))
for i in string.split("\n\n"):
    string2.append(i.replace('\n',''))

print(string2)




