#!/usr/bin/python
#source code to open my web stuffs

import webbrowser as wb
import sys

if len(sys.argv) > 1:
   if sys.argv[1]=='aasis21':
     wb.open('https://github.com/aasis21')
     print(sys.argv)
   elif sys.argv[1]=='lrn_py':
     wb.open('https://automatetheboringstuff.com/')
   else:
     wb.open('https://www.google.co.in')
else:
   wb.open('https://www.google.co.in')

