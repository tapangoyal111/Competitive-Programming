from bisect import bisect_right as br
import sys 
n=int(input())
a=[[] for i in range(n+1)]
d={}
e={}
ma={}
for i in range(n-1):
    x,y,z=map(int,sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)
    e[z]=e.get(z,[]) + [(x,y)]
par=[i for i in range(n+1)]
size=[1 for i in range(n+1)]
 
def findpar(x):
    while x!=par[x]:
        x=par[x]
    return x
 
s=0    
 
for i in sorted(e):
    ma[i]=s
    for k in e[i]:
        x,y=k
        px=findpar(x)
        py=findpar(y)
        par[px]=min(px,py)
        par[py]=min(px,py)
        ma[i]+=(size[px]*size[py])
        size[par[px]]=size[px] + size[py]
        s=ma[i]
        # print(ma)    
ma[0]=0
b=list(ma.keys())
b.sort()
# print(b)
for i in range(int(input())):
    x=int(sys.stdin.readline())
    ind=br(b,x)
    # print(ind)
    print(ma[b[ind-1]])
