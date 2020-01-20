dp=[0,"Pranshu","Jatin","Pranshu","Jatin","Jatin","Pranshu","Pranshu"]
 
def check(k,val):
    # print("dc",k,val)
    if k==1:
        a=[0,"Jatin","Jatin","Pranshu","Pranshu"]
        return a[ val]
    elif k==0:
        a=[0,"Jatin","Pranshu"]
        return a[ val]
    if val<=(2**k):
        return "Jatin"
    elif val<=(2**k + 2**(k-1)):
        return check(k-1,val - (2**k) + 2**(k-1))
    else:
        return check(k-2,val-((2**k) + 2**(k-1)))
 
 
 
 
for i in range(int(input())):
    p=int(input())
    if p<=7:
        print(dp[p])
    else:
        # p-=7
        if (p&(p+1))==0:
            print("Pranshu")
        else:
            for i in range(2,100):
                if (2**i) - 1>p:
                    # print(i-2, p - (2**(i-1)) + 1)
                    print(check(i-2,p - 2**(i-1) + 1))
                    # print("-------")
                    break
                    
 
