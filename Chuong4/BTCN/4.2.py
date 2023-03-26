def nhap():
    n=int(input('n='))
    return n 
def inkq(n):
    if n>=2:
        for i in range(2,n+1,2):
            print(i,end=" ")
    else:
        print( None)
while True:   
    n=nhap()
    inkq(n)
    tieptuc=input('tiep tuc khong?')
    if tieptuc=='K' or tieptuc=='k':
        break
 
