t = int(input())
for i in range(t):
    s = list(map(int,input().split()))
    s.sort()
    #print(s)
    if s[1]!=s[2]:
        print('NO')
    else:
        print('YES')
        print(s[0],s[0],s[2])
