            # VL01 - In ra các số từ a đến b
# a,b= input() .split()
# a=int(a)
# b=int(b)
# if -1000<=a<=b<=1000:
#     for i in range (a,b+1):
#         print(i,end=" ")
      # VL02 TÍNH TỔNG PHIÊN BẢN 1 s=1+2+3+4
# n=int(input())
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)
        # VL03 - Tính tổng S = (2 + 3 + 4... + n) + 2n

# cách tính tổng từ 1 đến n : n*(n+1)/2
# n=int(input())
# if n>=2 and n<=10**4:
#     s=0
#     for i in range (2,n+1):
#         s+=i
#     s+=2*n
#     print(s)    

            # VL04 - Tính tổng S = 1/2 + 1/3 + ... + 1/n
# n=int(input())
# s=0
# for i in range (2,n+1):
#     s+=1/i
# print('{:.4f}'.format(s))

      # VL05 - Tính giá trị S = 1 - 2 + 3 - ... + (3n + 1)
# n=int(input())
# s=0
# for i in range (1,3*n+2):
#     if i%2==0:
#         s-=i
#     else:
#         s+=i
# print(s)

       # GT01GT1 - Tính giai thừa 1

# n=int(input())
# if n<=12:
#     giaithua=1
#     for i in range (1,n+1):
#         giaithua*=i
#     print(giaithua)



       # vl08VL08 - Tính tổng các số chẵn trong [a, b]

# a,b=[int(x)for x in input().split()]
# s=0
# if -10000<=a<=b<=10000:
#     for i in range (a,b+1):
#         if i%2==0:
#             s+=i
#     print(s)

     # vl07Viết chương trình tính tổ hợp chập k của n phần tử có công thức như dưới đây:
# n, k=map(int, input().split())
# if 1<=k<=25 and 1<=n<=25:
#     n_=1
#     for i in range(1,n+1):
#         n_*=i
#     k_=1
#     for i in range(1,k+1):
#         k_*=i
#     n_k_=1
#     for i in range(1,(n-k)+1):
#         (n_k_)*=i
#     s=(n_//(k_*n_k_))
#     print(s)

    
             
      #   vl09 1/2 VL09 - Tính S = x + x^2/2! + ... + x^n/n!
# x,n=input().split()
# x=float(x)
# n=int(n)
# s=x
# giaithua=1
# if (-10<=x<=10)  and (n<=10):
   
#     for i in range (2,n+1):# không bắt đầu bằng 1 vì x^1/1!=x
#         giaithua*=i
#         s+= (x**i)/giaithua
#     print('{:.2f}'.format(s))

      # VL10 VL10 - Đếm số lượng chữ số của số n
n=int(input())
n=abs(n)
if n<=10**1000:
    if n==0:
        print(1)
    else:
        print(len(str(n).replace('-','')))
else:
    print()
        


# vl11 sai 3/6 VL11 - Kiểm tra số nguyên tố
# n=int(input())
# if abs(n)<=10**12:
#         if n<2:
#             print('NO')
#         else:
#             for i in range (2,n-1):
#                 if n%i==0:
#                     print('No')
#                     break
#             else:
#                 print('Yes')
            
            
            
            # vl12  4/5 VL12 - Liệt kê các ước số
# Viết chương trình liệt kê các ước nguyên dương của số nguyên n nhập từ bàn phím theo thứ tự giảm dần.
# n=int(input())
# i=n
# if (abs(n))<=10**4:
#     if n==0:
#         print('INF')
#     else:
#         for x in range (1,n+1):
#             if n%i==0:
#                 print(i,end=" ")
#             i-=1
                 
            # VL13 - Kiểm tra số hoàn hảo
# ươc của cố hoàn hảo là các số mà n chia hết cho nó (28=1+2+4+7+14)
# n=int(input())
# s=0
# if 0<=n<=10**9:
#     if n<=0:
#         print("NO")
#     for i in range (1,n):
#         if n%i==0:
#             s+=i
#     if s == n:       
#         print("YES") 
#     else:
#         print('NO')
# else:
#     print('NO')

            # VL14 - Tìm ước chung lớn nhất của 2 số
# Cho 2 số nguyên a và b, viết chương trình tìm ước chung lớn nhất của a và b
# def gcd(a,b):
#     a=abs(a)
#     b=abs(b)
#     if b==0:
#         return a
#     return gcd(b,a%b)
# a,b=[int(x)for x in input().split()]
# print(gcd(a,b))
    


            # VL15 - Rút gọn phân số a/b
# def gcd(a, b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# a,b=[int(i)for i in input().split()] 
# if a<0 or b<0:
#     if a>0 or b>0:
#         print('-',end=" ")   
# if b==0:
#     print('INVALD')
# elif a%b==0:
#     print(abs(int(a/b)))
# else:
#     a=abs(a)
#     b=abs(b)
#     x=gcd(a,b)
#     print(int(a/x),int(b/x))

# VL16 - Tìm bội chung nhỏ nhất của 2 số
# def gcd(a,b):
#     if b==0:
#         return(a)
#     return gcd(b,a%b)
# a,b=[abs(int(i)) for i in input().split()]
# print(int(a*b/gcd(a,b)))
     
#  VL17 - Đếm số lượng ước số
# a=abs(int(input()))
# s=0
# if a==0:
#     print(None)
# else:
#     if abs(a)<=1000:
#         for i in range(1,abs(a)+1):
#             if a%i==0:
#                 s+=1
#         print(s)


      # vl19 VL19 - In ra các số chia hết chia hết cho 3
# a,b= input().split()
# a=int(a)
# b=int(b)
# count=0
# if (a<=b)  :
#     for i in range (b-1,a,-1):
#         if i%3==0:
#             print(i,end=' ')
#             count+=1
# if a>=b:
#     print('NOT FOUND')
# if count==0:
#     print('NOT FOUND')


      # VL20 - In ra các chữ cái
# a,b=[x.upper() for x in input().split()]
# a=ord(a)
# b=ord(b)
# if a<b:
#     for i in range(a,b+1):
#             print(chr(i),end=" ")

# VL21 - Đi tìm ẩn số


      # SUM2 - Tính tổng phiên bản 2 
# n=int(input())
# s=0
# if 1<=n<=10**6:
#     for i in range(1,n+1):
#         s+=i**2
#     print(s)

      # SUM3 - Tính tổng phiên bản 3
# n=int(input())
# s=0
# if 1<=n<=10**6:
#     for i in range(1,n+1):
#         s+=1/(i*(i+1))
#     print('{:.5f}'.format(s))

      # SUM4 - Tính tổng phiên bản 4
# T=int(input())
# for _ in range (T):
#     n=int(input())
#     s=0
#     if 1<=T<=10**5 and 1<=n<=10**5:
#         for i in range(1,n+1):
#             c=1/(i*(i+1)/2)
#         print(c)




    

                          
