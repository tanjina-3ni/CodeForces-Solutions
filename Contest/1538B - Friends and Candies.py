t = int(input())

for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if n == 1 or len(set(a))==1:     # one person or everyone has same no. of candies
        print(0)
    elif s%n != 0:
        print(-1)
    else:
        s = int(s/n)
        x = 0
        y = 0
        c = 0
        for i in range(0,n):
            if a[i]>s:
                x = x + a[i] - s
                c = c + 1
            elif a[i]<s:
                y = y + s - a[i]
        if x==y:
            print(c)
        else:
            print(-1)
        