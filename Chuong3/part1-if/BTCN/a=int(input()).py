a=float(input())
b=float(input())
c=float(input())
a,b,c>0
if (a*a==b*b+c*c)or(c*c==a*a+b*b)or(b*b==a*a+c*c):
    print('Tam giac vuong')
elif a==b and b==c and c==a:
    print('Tam giac deu')
elif (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0):
    print('Tam giac loai khac')
else:
    print('Khong hop le')