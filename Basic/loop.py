
# L = [1,2,3,4,5]
# s = 0
# for a in L:
#     s += a
# print(s)

# L = [5,9,1,5,8]
# for item in range(len(L)):
#     print("L[{}] = ".format(item),L[item])

s = 0
for item in range(1,101):
    s += item
print(s)

L = [[5,9,1],[5,8]]
for i in L:
    for j in i:
        print(j)


for i in range(6):
    print("* "*i)
# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print()
print("@@@@@@@@@@@@@@")

# for i in range(5):
#     for j in range(5-i):
#         print(" ", end="")
#     for k in range(i+1):
#         print("* ", end="")
#     print("")
# # print("~~~~~~~~~~~~~~")
# for i in range(5):
#     for j in range(i):
#         print(" ",end="")
#     print("* "*(5-i))


# a = {"score": "98.50", "age": 17, "name": "lyh"}
# for item in a.values():
#     print(item)


# s = 0
# for i in range(1,11):
#     gender = input("请输入性别：")
#     age = int(input("请输入年龄："))
#     if gender == 'f' and age >= 10 and age <= 12:
#         s += 1
# print(s)

# # 100的和
# i = 1
# s = 0
# while i <= 100:
#     s = s+i
#     i += 1
# print(s)
#
# # 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(j,i,i*j),end=" ")
#     print("")

L= [9,78,33,6,23,5]
for j in range(len(L)):
    for i in range(len(L)-j-1):
        if L[i] > L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]
print(L)
