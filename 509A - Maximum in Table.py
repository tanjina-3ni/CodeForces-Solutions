s = 0
def func(a,b):
    global s
    if a==1 or b==1:
        s = s + 1
    else:
        a = a - 1
        
        while b:
            func(a,b)
            b = b - 1
    return


n = int(input())
func(n,n)
print(s)


