# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:27:56 2021

@author: Aspire
"""

n = input()
t = list(map(int,input().split()))

a = []
b = []
c = []

for i in range(0,int(n)):
    if t[i]==1:
        a.append(i)
    elif t[i]==2:
        b.append(i)
    else:
        c.append(i)

m = min(len(a),len(b))
m = min(m,len(c))
print(m)
for i in range(0,m):
    print(a[i]+1,b[i]+1,c[i]+1)

