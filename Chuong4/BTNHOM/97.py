import random
import re

def dkngaunhien():
    # Tạo một mật khẩu ngẫu nhiên với độ dài từ 8 đến 12 ký tự
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    length = random.randint(8, 12)#randint(a, b) sẽ trả về một số nguyên ngẫu nhiên nằm trong khoảng từ a đến b
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def ktmk(password):
    if len(password) < 8:
        return False
    
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

def inkq():
    count = 0
    while True:
        password = dkngaunhien()
        count += 1
        if ktmk(password):
            print("Mật khẩu mới của bạn là:", password)
            break
    print("Số lần thử cần thiết trước khi tạo ra mật khẩu mới là:", count)

inkq()
