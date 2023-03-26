# # n lên màn hình dãy số từ 1 đến n, với điều kiện mỗi số nằm trên một dòng văn bản
n=int(input('n='))
if n>=1:
    for i in range (1,n+1):
        print(i)


    # 3.10b
# n=int(input())
# if n>=1:
#     for i in range (1,n+1):
#         print(i,end=' ')
#         if i%5==0:
#             print()
        
        
# n=int(input())
# i=1
# while i<=n:
#     print(i,end=" ")
#     i=i+1
#     if i%5==0:
#         print(i)


#3.10.c
n=int(input())
if n>=1:
    for i in range (1,n+1):
        for j in range (1,n+1):
            print(j,end=" ")
        print()
    
    
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1
    
    
    
    
        
    
        
    
        