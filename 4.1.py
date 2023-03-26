def nhap():
    n=int(input('n='))
    return n 
def giaithua(n):
    if n==0:
        return 1
    else:
        giaithua=1
        for i in range(1,n+1):
            giaithua*=i
        return giaithua
    
def inkq(n,X):
    print(n,"!=",X,sep="")   
    
n=nhap()
kq=giaithua(n) 
inkq(n, kq)    