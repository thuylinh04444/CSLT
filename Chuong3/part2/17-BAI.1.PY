n=int(input('n='))
if n==0:
    print(n,"!=",1,sep="")
else:
    a=1
    for i in range (1,n+1):
        a*=i
    print(n,"!=",a,sep="")
    

        
