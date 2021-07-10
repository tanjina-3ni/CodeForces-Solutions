t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    c = 0
    ans = 0
    for k in range(n):
        if s[k]=='(':
            c += 1
        elif s[k]==')' and c>0:
            c -= 1
        else:
            ans += 1
    print(ans)
        