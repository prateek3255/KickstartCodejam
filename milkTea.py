import itertools
import sys
t=int(input())
def complaint(res,N):
    comp=0
    for i in N:
        for j in range(len(res)):
            if i[j]!=res[j]:
                comp+=1
    return comp


for t_itr in range(t):
    # Large dataset
    # n,m,p=map(int,input().split())
    # N=[]
    # M=[]
    # for _ in range(n):
    #     N.append(list(map(int,list(input()))))
    # for _ in range(m):
    #     M.append(list(map(int,list(input()))))
    # common=list(zip(*N))
    # res=[]
    # for i in common:
    #     res.append(max(set(i),key=i.count))
    # if res not in M:
    #     print("Case #{}: {}".format(t_itr + 1, complaint(res,N)))
    # else:
    #     d={}
    #     for i in range(len(common)):
    #         d[i]=abs(common[i].count(0)-common[i].count(1))
    #     x=list(sorted(d,key=d.__getitem__))
    #     print(d,x)

    # small dataset
    n,m,p=map(int,input().split())
    N=[]
    M=[]
    for _ in range(n):
        N.append(list(map(int,list(input()))))
    for _ in range(m):
        M.append(list(map(int,list(input()))))
    comb=list(itertools.product([0,1],repeat=p))
    minComplaints=sys.maxsize
    for i in comb:
        if list(i) not in M:
            comp=complaint(i,N)
            if comp<minComplaints:
                minComplaints=comp
    print("Case #{}: {}".format(t_itr + 1, minComplaints))

