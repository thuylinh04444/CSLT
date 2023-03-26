import re #là module cho phép sử dụng biểu thức chính quy (regular expressions)

def mk(password):
    if len(password) < 8:
        return False
    if not ktmk(password):
        return False
    return True

def ktmk(password):
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

def inkq():
    password = input("Nhập mật khẩu: ")
    if mk(password):
        print("Mật khẩu của bạn là tốt.")
    else:
        print("Mật khẩu của bạn không đủ mạnh.")  
 
        
inkq()










# def mk(password):
#     password=input()
#     if len (password)<8:
#         return False
    
# def ktmk(password):
#     hoa = False
#     thuong =False
#     so = False
#     for char in password:
#         if char.isupper():
#             hoa=True
#         elif char.islower():
#             thuong=True
#         elif char.isnumeric():
#             so=True
#     return hoa, thuong,so

# def inkq(hoa,thuong,so):
#     if hoa and thuong and so:
#         return True
#     else:
#         return False

# def dk():
#     password=mk()
#     if not password:
#         print('mat khua qua ngan') 
#         return
#     hoa,thuong,so =ktmk(password)
#     inkq(hoa,so,thuong)
# if __name__ == '__main__':
#     main()

