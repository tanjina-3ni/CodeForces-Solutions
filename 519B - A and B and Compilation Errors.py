t = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
for k in range(len(a)):
    if k==len(a)-1:
        print(a[k])
    elif a[k] != b[k]:
        print(a[k])
        break
for k in range(len(b)):
    if k==len(b)-1:
        print(b[k])
    elif c[k] != b[k]:
        print(b[k])
        break