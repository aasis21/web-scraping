#!/usr/bin/python3
#get txt downloaded
import requests
res=requests.get('http://home.iitk.ac.in/~arlal/MTH102/LA_Assignments/PS1.pdf')
try:
    res.raise_for_status()
except Exception as ex:
    print(ex)

pfile=open('assgn12.txt','wb')
for chunk in res.iter_content(100000):
    pfile.write(chunk)
pfile.close()
