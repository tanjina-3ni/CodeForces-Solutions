# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:26:03 2021

@author: Aspire
"""

s1 = 'I hate '
s2 = 'I love '
s3 = 'that '
s4 = 'it '
s = ''
n = int(input())

for i in range(1,n+1):
    if i==1:
        s = s1
    elif i%2 == 0:
        s = s + s3 + s2
    elif i%2 != 0:
        s = s + s3 + s1
    
        
s = s + s4
print(s)