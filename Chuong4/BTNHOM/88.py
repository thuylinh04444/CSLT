def nhap ():
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    return a,b,c 
    
def tamgiac(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return False
    else:
        return True
def inkq(kq,a,b,c):
    if tamgiac(a,b,c):
        print('ba canh nay co the tao thanh tam giac deu')
    else:
        print('ba canh nay khong the tao thanh tam giac deu ')
        
n=nhap()
a,b,c=n 
kq=tamgiac(a,b,c)
inkq(kq,a,b,c)
            