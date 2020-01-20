import sys
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
    b.append(a[-1][i])
xor=[[] for i in range(1002)]
for  i in range(int(input())):
    w,x,y,z=map(int,sys.stdin.readline().split())
    xor[x-1].append(z)
    xor[y].append(z)
ans=0
an=0
    
# print(xor[:20])
for i in range(n):
    for k in (xor[i]):
        an^=k
    ans+=(b[i]^an)
    
print(ans)
