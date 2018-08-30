t=int(input())
for t_itr in range(t):
    n,k=map(int,input().split())
    y=list(map(int,input().split()))
    y.sort()
    yogurt=0
    x=0
    end=False
    for i in range(n):
        for _ in range(k):
            if x<n and y[x]>i:
                yogurt+=1
                x+=1
            else:
                while x<n and y[x]<=i:
                    x+=1
                if x<n:
                    yogurt+=1
                    x+=1
                else:
                    end=True
                    break
        if end:
            break

    print("Case #{}: {}".format(t_itr + 1, yogurt))
