# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:11:15 2021

@author: Aspire
"""

sn = list(map(int,input().split()))
s = sn[0]
c = 0
xyl = []
for i in range(0,sn[1]):
    xy = list(map(int,input().split()))
    xyl.append(xy) 
xyl.sort()
i = 0
while(i<sn[1]):
    if s>xyl[i][0]:
        s = s + xyl[i][1]
    else:
        c = 1
        break
    i = i + 1
    

if c==1:
    print('NO')
else:
    print('YES')

        