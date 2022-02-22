import os
# 文件操作
file = open("new.txt",'a',encoding="utf-8")
# print(file.read())
print("-----------")
# print(file.readline())
print("-----------")
# print(file.readlines())

# file.write("hcy/")
# file.writelines(["\n","hcy\n","蔡徐坤"])

# 文件夹操作
# os.mkdir("nic")
# os.mkdir("D:\eclipse2\lyh")
# os.rmdir("nic")

# 获取当前工作目录
path = os.getcwd()
print(path)

# 获取当前类的路径
path_1 = os.path.realpath(__file__)
path_2 = os.path.relpath(__file__)
print(path_1)
print(path_2)

# join拼接路径
new_path = os.path.join(os.getcwd(), "python1001",'sub_1')
# os.mkdir(new_path)
print(new_path)

# 判断是文件还是目录
print(os.path.isdir(os.getcwd()))
print(os.path.isfile(__file__))

# 判断是否存在
flag = os.path.exists("D:\Python\Study\File\\file_test.py")
print(flag)

# 罗列目录下所有的文件和目录
print(os.listdir(os.getcwd()))
