n,t = map(int,input().split())
a = list(map(int,input().split()))
i = 0
f = 0
while i<t:
    #print(a[i]+i+1)
    if a[i]+i+1 == t:
        f = 1
        break
    i = a[i]+i
if f==0:
    print('NO')
else:
    print('YES')