t = int(input())
for i in range(0,t):
    n = int(input())
    s = list(map(int,input().split()))
    setofs = list(set(s))
    if s.count(setofs[0])==1:
        print(s.index(setofs[0])+1)
    else:
        print(s.index(setofs[1])+1)
