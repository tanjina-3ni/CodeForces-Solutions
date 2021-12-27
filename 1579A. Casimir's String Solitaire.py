t = int(input())

for i in range(0,t):
    s = input()
    if s.count('A')+s.count('C')==s.count('B'):
        print('YES')
    else:
        print('NO')