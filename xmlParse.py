#importing re(Regular Expressions), BeautifulSoup and urllib will work
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#same can be done from other methods. Resource: https://www.py4e.com/code3/geoxml.py
url = input("Enter URL here: ")            #URL samples: http://py4e-data.dr-chuck.net/comments_42.xml
                                           #             http://py4e-data.dr-chuck.net/comments_64376.xml
html = urllib.request.urlopen(url).read()  #reading the webpage data as a string with \n characters
soup = BeautifulSoup(html, 'lxml')         #building tree to extract tags

count = 0
tags = soup('count')
lst= list()
for tag in tags:
	count = count + 1
	x = re.findall(('>(\S+)<'), str(tag))  #using re to return a list
	                                       #list consists of retrieved values inside tags
	lst.append(int(x[0]))
print('Count: ', count)
print('Sum: ', sum(lst))
#summing and printing of all list elements