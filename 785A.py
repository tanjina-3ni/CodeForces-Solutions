# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:10:14 2021

@author: Aspire
"""

polygon = [4, 6, 8, 12, 20]

t = int(input())
face = 0

for i in range(0,t):
    p = input()
    if p == 'Tetrahedron':
        face = face + polygon[0]
    elif p == 'Cube':
        face = face + polygon[1]
    elif p == 'Octahedron':
        face = face + polygon[2]
    elif p == 'Dodecahedron':
        face = face + polygon[3]
    else:
        face = face + polygon[4]

print(face)