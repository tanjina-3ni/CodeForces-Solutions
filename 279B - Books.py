n,t = map(int,input().split())

a = list(map(int,input().split()))

summ = 0
c = 0
maxx = -1
i = 0
j = 0
while i<n:
    summ += a[i]
    c += 1
    if summ<=t:
        if maxx<c:
            maxx=c
    else:
        summ -= a[j]
        c = c - 1
        j += 1
    i += 1
print(max(maxx,c))