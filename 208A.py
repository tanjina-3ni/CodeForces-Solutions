# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:32:34 2021

@author: Aspire
"""
import re
#newstring = re.sub(' +', '_', input1)
s = input()
s = ''.join(map(str, s)) 
#print(s)
s = s.replace('WUB',' ')
s = re.sub(' +', ' ', s)

res = ''
if s[0]==' ':
    
    s = s[:0] + s[1:]
print(s)

    
            
