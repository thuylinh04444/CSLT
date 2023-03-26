# n = int(input("n= "))
# chuso= 0
# i=1
# if n >= 0 and  n<=9999:
#     while True:
#         if n//i!=0:
#             chuso+=1
#             i*=10
#         else:
#             break
#     print(n,'co',chuso,'chuso')
                    
n=int(input())
n=abs(n)
if n<=10**1000:
    if n==0:
        print(1)
    else:
        print(len(str(n).replace('-','')))
else:
    print()