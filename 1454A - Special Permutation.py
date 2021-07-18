t = int(input())
for i in range(t):
    n = int(input())
    s = ''
    for k in range(n-1):
        s = s + str(k+2) + " "
    s += '1'
    print(s)