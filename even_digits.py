
def check_even(k):
    l=[int(i) for i in str(k)]
    for i in l:
        if i%2!=0:
            return False
    return True

n=int(input())
for test in range(n):
    m=int(input())
    s=int(m)
    l=int(m)
    while not(check_even(s) or check_even(l)):
        s=s-1
        l=l+1
    res=min(m-s,l-m)
    print("Case #{}: {}".format(test+1, res))
        






