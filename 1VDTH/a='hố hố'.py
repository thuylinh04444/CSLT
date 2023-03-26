# baif 1
# A=int(input())
# B=int(input())
# s=0
# if A<=B:
#     for i in range (A+1,B+1):
#         s+=i
#     print(s)
# else:
#     print(None)
# baif 2
# n=int(input())
# s=0
# if n<0:
#     print(None)
# else:
#     if 0<=n<=10**6:
#         for i in range (1,n+1):
#             if i%3==0 and i%5==0:
#                 s+=1
#         print(s)    
#     else:
#         print(None)

# baif 3
# a=int(input())
# b=int(input())
# n=int(input())

# if a+b==n:
#     print('+')

# elif a-b==n:
#     print("-")

# elif a*b==n:
#     print('*')

# elif a>=b:
#     if a/b==n:
#         print("/")
#     else:
#         print('NO')
# else:
#     print('NO')



    # nbaif 5
# n=int(input())
# s=0
# if 1<=n<=10**6:
#     for i in range(1,n+1):
#         if i%2==0:
#             s+=i  
#     print(s)
# else:
#     print(None)
# baif 4            # 
n=(input())
n=int()
if n<10**6:
    if 0<n<10:
        print('0')
else:
       sochu1=(n%100)%10
       sochu2=(n%100)//10
       tong=sochu1+sochu2
       print(tong)
                
        
        
   


    