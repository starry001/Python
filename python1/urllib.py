import urllib
o = urllib.parse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(o)
print(o.path)
print(o.scheme)
print(o.port)
print(o.geturl())