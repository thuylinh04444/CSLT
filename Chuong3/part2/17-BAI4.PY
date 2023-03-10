while True :
    a=int(input('a='))
    b=int(input('b='))
    c=input('toantu')
    if c== '+':
         ket_qua=a+b
    elif c=='-':
        ket_qua=a-b
    elif c=='*':
        ket_qua=a*b
    elif c=="/":
        if b==0 :
            break
        else:
           ket_qua=a/b
    else:
        continue
    print(a,"+",b,ket_qua)
    
    tieptuc=input('tieptuc')
    if tieptuc=='t' or tieptuc=='T':
        break
    
    

        

        
    

  
   
  
    


    