        #cb1 tongr 2 so nguyen 
# a,b=[int(x) for x in input().split()]
# print(a+b)

            #cb2 tinh tong 3 so nguyen#
# a,b,c=[int(x) for x in input().split()]
# print(a+b+c)

            #cb3 tinh tong tich hieu chia
# a,b=[int(x) for x in input() .split()]
# if abs(a)<=100 and abs(b)<=100 :
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     if b!=0:
#         print("{:.2f}".format(a/b))
#     else:
#         print('INF')

            #cb4 tìm số dư 
# a,b =[int(x) for x in input().split()]
# if 0<a<1000000 and 0<b<1000000:
#     if b!=0:
#         print(a%b)
 
            #cb5 tính chu vi dien tich chu vi hình chu nhat 
# r,d=[int(x) for x in input().split()]
# if 0<r<=5000 and 0<d<=5000:
#     print((r+d)*2)
#     print(r*d)
    
            #cb06 tinh diện tích và chu vi hình tròn 
# r=float(input())
# pi=3.14
# chuvi=1
# dientich=1
# if 0<r<1000:
#     chuvi=(r*2)*pi
#     dientich=r**2*pi
#     print("{:.3f}".format(chuvi))
#     print("{:.3f}".format(dientich))

            #  cb07 tinh tỏngo hien thị phép tính 
# a,b= input().split()
# a=int(a)
# b=int(b)
# if abs(a)<=10**9 and abs(b)<=10**9:
#     print(a,"+",b,"=",a+b)

            # PHTINH - Phép toán lớp 3
# a,b=[int(x)for x in input().split()]
# if -10<=a<=10 and -10<=b<=10:
#     if a*b>0:
#         print('1')
#     elif a*b<0:
#         print('-1')
#     else:
#         print('0')
        
        # PTIT023 - Bạn bao nhiêu tuổi?
# print(2021-int(input()))

            # PTIT051 - Hoàn thành câu lệnh
# date,month,year = map(int,input().split())
# print("users setClock " + chr(92) + str(month) + chr(92) + str(date) + chr(92) + str(year))

        
            
            #GAPDOI SỐ GAP ĐÔI
# a=int(input())
# if abs(a)<=100:
#     print(a*2)
# else:
#     print()        

            # AVG3NUM - Trung bình cộng của 3 số
# a,b,x=[int(x)for x in input().split()]
# if (1<=a<=100)  and (1<=b<=100)  and  (1<=x<=100)  :
#     print((3*x)-a-b)
# else:
#     print((3*x)-a-b)

            #FUNCTION - Tính giá trị hàm bậc 2
# a,b,c,x=[int(x) for x in input().split()]
# if 0<=a<=10**6 and 0<=b<=10**6 and 0<=c<=10**6 and 0<=x<=10**6 :
#     print(a*x**2+b*x+c)
    
                # PREP - Chuẩn bị cho năm học mới
# a,b,x,y=map(int,input().split())
# s=(a*x)+(b*y)
# print(s)
      #     PTIT028 - Làm tròn số

#     import math

# x = float(input())  # nhập số thập phân

# # Tìm số nguyên nhỏ nhất lớn hơn x
# lower = math.ceil(x)

# # Tìm số nguyên lớn nhất bé hơn x
# upper = lower - 1

# # In ra hai số nguyên
# print(lower, upper)
    
    
