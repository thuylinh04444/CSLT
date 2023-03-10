n = int(input("n= "))
chuso= 0
i=1
if n >= 0 and  n<=9999:
    while True:
        if n//i!=0:
            chuso+=1
            i*=10
        else:
            break
    print(n,'co',chuso,'chuso')
                    
