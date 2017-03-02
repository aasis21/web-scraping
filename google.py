#!/usr/bin/python3
#google command line argument and opens all in new tabs....cooool....
import sys,webbrowser,requests,bs4

print('Goooogling......')
#get site source code ofline...
res=requests.get('https://www.google.co.in/search?q='+''.join(sys.argv[1:]))
webbrowser.open('https://www.google.co.in/search?q='+''.join(sys.argv[1:]))

res.raise_for_status()
#get soup object passing the txt string
soup=bs4.BeautifulSoup(res.text)
r_list=soup.select('.r a')
#a list of corresponding results...
#opening all in new tab..
ct=min(5,len(r_list))
for i in range(ct):
    webbrowser.open('https://www.google.com'+r_list[i].get('href'))
                    
