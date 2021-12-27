t = int(input())
for i in range(0,t):
    n = int(input())
    l = list(map(int,input().split()))
    if sum(l)%2==0:
        o = 0
        e = 0
        for j in range(0,n):
            if l[j]%2==0:
                e += 1
            else:
                o += 1
        if o>=1 and e>=1:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')