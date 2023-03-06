M1=int(input('M1='))
M2=int(input("M2="))
M3=int(input("M3="))
s=int(input("S="))
if s<=100:
    print('Phai tra=',s*M1,sep=(''))
elif 101<=s<=150:
    print('Phai tra=',(M1*100)+((s-100)*M2),sep=(""))
else:
    print('Phai tra=',(M1*100)+(M2*50)+((s-150)*M3),sep=(''))


