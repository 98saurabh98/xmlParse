# xmlParse
Parsing XML data using BeautifulSoup and urllib

import re(Regular Expressions), BeautifulSoup and urllib
Takes URL input
URL samples: http://py4e-data.dr-chuck.net/comments_42.xml
             http://py4e-data.dr-chuck.net/comments_64376.xml

Reads webpage data as a single string(because of .read() method)
uses re to search through strings and returns a list of required output
'>(\S+)<'   =>    Search for a string starting with > and ending with < and in between it can have one or more non-whitespace characters. Parenthesis is used to return the required values.
Finally append all elements to single list and sums them all and returns 'sum'


There is another method of doing this. Resource : https://www.py4e.com/code3/geoxml.py
