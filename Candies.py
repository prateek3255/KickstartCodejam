#https://code.google.com/codejam/contest/6364486/dashboard
n,o,d=map(int,input().split())
x1,x2,a,b,c,m,l=map(int,input().split())
x=[x1,x2]
for i in range(2,n):
    x.append((a*x[i-1]+b*x[i-2]+c)%m)
s=[i+l for i in x]

