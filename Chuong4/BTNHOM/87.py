def cangiua(string,width): #string: chuoi dau vao width: chieu rong cua thiet bi dau cuoi
    l=len(string)
    if l>= width :
        return string 
    else:
            dodai = width - len(string)
            left_ = dodai // 2
            right_ = dodai - left_
            result = string.center(width)
            return result

string = "cslt kho qua di"
width = 40

kq = cangiua(string, width)
print(kq)














# def cangiua(string, width):
#     khoangtrang = max(0, width - len(string)) // 2
#     s = ''
#     for i in range(khoangtrang): #để thêm số lượng ký tự khoảng trắng vào đầu hoặc cuối chuỗi ban đầu
#         s += ' '
#     s += string
#     for i in range(khoangtrang):
#         s += ' '
#     return s

# kq = cangiua("Hello", 20)
# print(kq)


