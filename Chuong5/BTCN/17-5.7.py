n=int(input("n="))
L=[]
for i in range(0,n):
    x=int(input())
    L=L+[x]
A=[]
for k in L:
    if k not in A:
        A=A+[k]
    # if L.count(k)>=2:
    #     L.remove(k)
    #     L.sort() 
    # M=L    
print(A)