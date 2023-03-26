import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    delta=b**2-4*a*c  
    if delta<0:
        print('Phuong trinh vo nghiem')  
    elif delta==0:
        x=-b/2*a
        print(f"phuong trinh co nghiem kep")
        print(f'x1=x2={x}')
    else:
        print(f'Phuong tirnh co hai nghiem ')
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f' x1={x1}')
        print(f' x2={x2}')
def inkq(x1,x2):
    if x1==None and x2==None:
        print('Phuong trinh vo nghiem')
    elif x1==x2:
        print(f'Phuong trinh co nghiem kep{x1}')
        print(f'x1=x2={x1}')
    else:
        print(f'Phuong tirnh co hai nghiem ')
        print(f' x1={x1}')
        print(f' x2={x2}')
        
        
a,b,c=nhap()
kq=giaipt(a,b,c)


     