soduong=0
soam=0
while True:
    n=int(input())
    
    if n==0:
        break
    
    if n>0:
        soduong+=1
        
    else:
        soam+=1
        
print(f'{soduong} so duong')
print(f'{soam} so am')