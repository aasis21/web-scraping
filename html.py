#!/usr/bin/python3
import sys,webbrowser,requests,bs4
res=requests.get('https://www.google.co.in/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
webbrowser.open('https://www.google.co.in/search?q='+''.join(sys.argv[1:]))
myfile=open('html','wb')
for ck in res.iter_content(50000):
  myfile.write(ck)
myfile.close()
