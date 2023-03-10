  
# n=int(input("n="))
# import math
# for i in range(2,int(math.sqrt(n))+1):
#            #Kiem tra tinh chia het
#            if n % i == 0:
#                print("khong la so nguyen to!")
#                #Thoat vong lap
#                break
#        #Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
# else:
#            print("la so nguyen to!")
n=int(input('n='))
for i in range (2,n-1):
    if n%i==0 :
        print(n,'khong la SNT')
        break
else:
        print(n,'la SNT')