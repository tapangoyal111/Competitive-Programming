#/////////////////////////////////////////////////////////////////////////////////////////////////
import sys
 
# Fenwick Tree Implementation Index starts from 1
 
n=10**5 +1
 
pr=[0]*(10**5 + 1)
b=[]
a=[[] for i in range(10**5 + 1)]
for i in range(2,10**5 +1):
    if pr[i]==0:
        b.append(i)
        a[i].append(i)
        for j in range(2*i,10**5 + 1,i):
            if 1:
                pr[j]=1
                a[j].append(i)
                
 
# print(len(b))
            
        
 
def getsum(bit,ind):
    ans=0
    while ind>0:
        ans+=bit[ind]
        ind-=(ind&(-ind))
    return ans
 
 
 
def update(bit,ind ,val):
    while ind<=n:
        bit[ind]+=val
        ind+=(ind&(-ind))
 
 
 
def sumx(bit1,bit2,x):
    return (getsum(bit1,x)*x  - getsum(bit2,x))
 
###
def update_range(bit1,bit2,x,l,r):
    update(bit1,l,x)
    update(bit1,r+1,-x)
    update(bit2,l,x*(l-1))
    update(bit2,r+1,-x*r)
 
 
    
 
def get_range_sum(bit1,bit2,l,r):
    return sumx(bit1,bit2,r) - sumx(bit1,bit2,l-1);
 
###
 
bit=[0]*(3* (10**5 + 1))
 
 
 
for i in range(int(input())):
    l=list(map(int,sys.stdin.readline().split()))
    if l[0]==1:
        for j in a[l[1]]:
            update(bit,j,1)
    else:
        sys.stdout.write(str(getsum(bit,l[2]) - getsum(bit,l[1] - 1) ) + "\n")
        # ind1=bl()
 
# n=20
# bit1=[0]*(100)
# bit2=[0]*(100)
 
# update_range(bit1,bit2,5,1,4)
# update_range(bit1,bit2,3,3,6)
# update_range(bit1,bit2,1,5,7)
 
# print(get_range_sum(bit1,bit2,1,1))
    
    
    
        
 
