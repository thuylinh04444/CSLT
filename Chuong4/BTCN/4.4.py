def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    max=a
    if b>max:
        max=a
    if c>max:
        max=c
    return max
def inkq(kq):
    print(f'So lon nhat la: {kq}',sep="")
    
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)