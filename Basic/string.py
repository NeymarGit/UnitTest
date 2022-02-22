# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
a = 1;
# a = 3;
q_i = 2
print(a/2)
c = True
D = False

f = """I dont want see you anymore!!"""
print(f)
print(type(f))
print(len(f))

print(f[2:6:2])
# 倒序输出两种方法
print(f[::-1])
print(f[-1:-30:-1])

# 返回列表类型,不传参就默认按照空格分割
print(f.split())
print(f.split(' '))

# replace（指定替换值，新值，替换次数）
j = f.replace('t','X',1)
print(j)

# strip 去除指定字符,默认去掉空格,只能去掉首尾的
n = 'inter job'
print(len(n))
k = n.strip('i')
print(len(k))

# 字符串拼接
print(n,f)

# 字符串格式化输出,format
age = 17
name = 'lyh'
print("{}今年{}岁了".format(name,age))
print("%s今年%d岁了"%(name,age)) #


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
