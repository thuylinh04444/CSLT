                #dk01 tìm số lớn  nhất 
# a,b=[int(x) for x in input() .split()]
# if a>b:
#     max=a
# else: 
#     max=b
#     print(max)

#DK02 TÌM SỐ LỚN NHẤT TRONG 3 SỐ
# a,b,c=[int(x) for x in input().split()]
# print(max(a,b,c))

#DK03 TÌM GIÁ TRỊ CHÊNH LỆCH GIỮA HAI SỐ
# a,b=[int(x) for x in input().split()]
# if abs(a)<=10**6 and abs(b)<=10**6:
#     if a>b:
#         print(a-b)
#     else:
#         print(b-a)

# a,b = [int(x) for x in input().split()]
# print(abs(a-b))

#DK04 LÀM TRÒN SỐ 6/7
# n=float(input())
# if abs(n)<=10**6:
#     print('{:.0f}'.format(n))
# else:
#     print()
    
    #DK05 KIIỂM TRA SỐ CHÍNH PHƯƠNG 
# import math   
# n=int(input())
# if abs(n)<=10**12:
#     if n>=0:
#         x=math.sqrt(n)
#         if x==int(x):
#             print('YES')
#         else:
#             print('NO')
#     else:
#         print('NO')

#DK06 GIAI  PHUONG TRINH BAC 1 ẨN
# a,b=[int(x)for x in input().split()]
# if (abs(a))<=1000 and (abs(b))<=1000:
#     if a==0 and b!=0:
#         print('NO')
#     elif a==0 and b==0:
#         print('INF')
#     else:
#         print('{:.2f}'.format(-b/a))



# DK07 - Giải phương trình bậc 2
# a,b,c= input().split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a==0:
#         if  b==0 and c!=0 :
#             print("NO")
#         if b!=0 and c==0:
#             print('0.00')
#         if b==0 and c==0:
#             print("INF")
#         if b!=0:
#             print(round(-b/c,2))
# if a!=0:
#         import math 
#         d=b**2-4*a*c                        
#         if d<0:
#             print('NO')
#         if d==0:
#             print(round(-b/(2*a),2))
#         else:
#             x=(-b+math.sqrt(d))/(2*a)
#             y=(-b-math.sqrt(d))/(2*a)
#             if x<y:
#                 print('{:.2f}'.format(x))
#                 print('{:.2f}'.format(y))
#             else:
#                 print("{:.2f}". format(x), "{:.2f}". format(x))
    
            # DK08 - Máy tính bỏ túi đơn giản

# a,c,b=input().split()
# a= float(a)
# b=float(b)
# if abs(a )<=10000 and abs(b)<=10000:
#     if c=='+':
#         print('{:.2f}'.format(a+b))
#     if c=='-':
#         print('{:.2f}'.format(a-b))
#     if c=='*':
#         print('{:.2f}'.format(a*b))
#     if c=='/':
#         if b == 0:
#             print('Math Error')

#         else:
#              print('{:.2f}'.format(1.0*a/b))


            # PTIT033 SOỐ CHIA HẾT HAY KHÔNG 18/22
# n=int(input())
# a,b=map(int,input().split())
# if 1 <= n <= 10**18 and 1 <= a <= 10**18 and 1 <= b <= 10**18:
#     if n%a==0:
#         if  n%b==0:
#             print('Co, tat ca!')
#         elif  n%b!=0:
#             print('Chi chia het cho',a,",",sep='')
#     else:
#         if  n%b==0:
#             print('Chi chia het cho ',b,".",sep='')
#         else:
#             print('Khong chia het cho so nao ca',".",sep='')
# else:
#     print('Khong chia het cho so nao ca',".",sep='')
# if a>b:
#     a,b=b,a

    

                # DK09 - Kiểm tra năm nhuận
# n = int(input())
# if n <= 0 or n > int(10**5):
#     print("INVALID")
# elif (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#     print("YES")
# else:
#     print("NO")

                # DK10 - Tìm số ngày của tháng
# month, year = [int(x) for x in input().split()]
# list31 = [1,3,5,7,8,10,12]
# list30 = [4,6,9,11]
# if (month <= 0 or month > 12) or (year <= 0 or year > 100000):
# 	print('INVALID')
# else:
# 	if month in list31:
# 		print('31')
# 	elif month in list30:
# 		print('30')
# 	else:
# 		if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
# 			print('29')
# 		else:
# 			print('28')

            # TAMGIAC - Kiểm tra tam giác hợp lệ
# a,b,c = map(int,input().split())
# import math
# if a+b>c and b+c>a and a+c>b:
#     p = (a+b+c)/2
#     print(a+b+c, "{:.2f}". format(math.sqrt(p*(p-a)*(p-b)*(p-c))))
# else: print("NO")
            #    DK04 - Làm tròn số

# n = float(input())
# rounded_n = round(n)
# print(rounded_n)






