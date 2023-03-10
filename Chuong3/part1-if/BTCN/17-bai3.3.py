x=float(input("x="))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch== "+":
     print(x,ch,y,"=",round((x+y),1),sep='')
elif ch=="-":
      print(x,ch,y,",",round((x-y),1),sep='')
elif ch=="*":
        print(x,ch,y,",",round((x*y),1),sep='')
elif ch== "/" and y!=0: 
     print(x,ch,y,',',round((x/y),1),sep='')
else:
    print('Khong hop le')
          
# x=float(input('x='))
# y=float(input('y='))
# ch=str(input('Phep toan:'))
# if ch=='+':
#     print(x,ch,y,'=',x+y,sep='')
# elif ch=='-':
#     print(x,ch,y,'=',x-y,sep='')
# elif ch=='*':
#     print(x,ch,y,'=',x*y,sep='')
# elif y !=0 and ch=='/':
#     print(x,ch,y,'=',x/y,sep='')
# else:
#     print('Khong hop le')
                  