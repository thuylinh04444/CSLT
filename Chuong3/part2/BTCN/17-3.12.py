# n=int(input())
# bangmahoa={
#     0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'K',9:'L'}

# truyxuat=bangmahoa 
# hopchua=''# cai can in ra 
# for i in range (truyxuat):
#     hopchua+=bangmahoa[int(i)]
#     print(hopchua)
    
    
# # n = int(input())
# n_str = str(n)
# mh = ''
# for char in n_str:
#     if char == '0':
#         mh += 'A'
#     elif char == '1':
#         mh += 'B'
#     elif char == '2':
#         mh += 'C'
#     elif char == '3':
#         mh += 'D'
#     elif char == '4':
#         mh += 'E'
#     elif char == '5':
#         mh += 'F'
#     elif char == '6':
#         mh += 'G'
#     elif char == '7':
#         mh += 'H'
#     elif char == '8':
#         mh += 'K'
#     elif char == '9':
#         mh += 'L'
# print(mh)

n=int(input())
l=list(str(n))
if 0<=n<=9999:
    for i in range(0,len(l)):
        b=l[i] # tìm các phần tử trong list l để tương ứng với các giá trị
        if b=="0":
            print("A",end="")
        elif b=="1":
            print("B",end="")
        elif b=="2":
            print("C",end="")
        elif b=="3":
            print("D",end="")
        elif b=="4":
            print("E",end="")
        elif b=="5":
            print("F",end="")
        elif b=="6":
            print("G",end="")
        elif b=="7":
            print("H",end="")
        elif b=="8":
            print("K",end="")
        elif b=="9":
            print("L",end="")