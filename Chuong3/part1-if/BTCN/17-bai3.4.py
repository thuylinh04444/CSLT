a=int(input())
b=int(input())
c=int(input())
d=((a*2)+(b*3)+c)/6
if d<3:
    print('Kem')
elif 3<=d<5:
    print('Yeu')
elif 5<=d<6:
    print('Trung Binh')
elif 6<=d<7:
    print('Trung binh Kha')
elif 7<=d<8:
    print('Kha')
elif 8<=d<9:
    print('Gioi')
else:
    print('Xuat Sac')