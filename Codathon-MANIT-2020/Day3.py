n,m,l=map(int,input().split())
a=list(map(int,input().split()))
dp=[[0 for i in range(m)] for k in range(n)]
m1=[0]*m
for i in a:
    m1[i%m]+=1
mod=10**9 + 7
for i in range(m):
    dp[0][i]=m1[i]
 
# print(m1)
for i in range(1,n):
    for j in range(m):
        for k in range(m):
            dp[i][j]+=dp[i-1][(m-k)%m] * m1[(j+k)%m]
            dp[i][j]%=mod
 
 
# print(dp)
print(dp[n-1][0]) 
