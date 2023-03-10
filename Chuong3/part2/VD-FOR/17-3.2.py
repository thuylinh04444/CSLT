# n=int(input('n='))
# for i in range (1,46,1):
#     print(i,end=" ")
#     i=i+1
# if i%10==1:
#      print(i,end=" ")
# print()
n = int(input("n="))
for i in range(1, n + 1):
    if i % 10 == 0:
        print(i)
    else:
        print(i, end=" ")