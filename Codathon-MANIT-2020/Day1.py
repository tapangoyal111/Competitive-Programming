n,k=map(int,input().split())
a=[]
for i in range(n):
	a.append(int(input()))
while(a):
    if a[-1]>k:
        break
    a.pop()
while a:
    if a[0]>k:
        break
    a.pop(0)
print(len(a))    
