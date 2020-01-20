n=int(input())
s=input()
x,y=map(str,input().split())
ans=0
if x not in s:
    print(0)
    exit()
ind=s.index(x)    
ans=1
ans1=0
mod=10**9 + 7
if x==y:
    # for i in range()
    ans1=s.count(x)
for i in range(ind+1,len(s)):
    if s[i]==y:
        ans1+=ans
    ans*=2
    if s[i]==x:
        ans+=1
    ans%=mod
    ans1%=mod
    # print(ans)        
print(ans1)        
        
        
