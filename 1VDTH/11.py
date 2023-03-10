n = int(input("Nhập số nguyên n: "))
encoded = ""

for i in str(n):
    if i == "0":
        encoded += "A"
    elif i == "1":
        encoded += "B"
    elif i == "2":
        encoded += "C"
    elif i == "3":
        encoded += "D"
    elif i == "4":
        encoded += "E"
    elif i == "5":
        encoded += "F"
    elif i == "6":
        encoded += "G"
    elif i == "7":
        encoded += "H"
    elif i == "8":
        encoded += "K"
    elif i == "9":
        encoded += "L"

print("Mã hóa của {}: {}".format(n, encoded))
