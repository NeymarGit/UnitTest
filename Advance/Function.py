# 函数

# 不定长参数
def student(*args):
    # *args传过来的是元祖
    all = ""
    for item in args:
        all += item
        all += "、"
    print("1202班的"+all)

student("lyh","scy","hmj")


def sum(n,m=1,k=1):
    s = 0
    for a in range(1,n+1,k):
        s += a
    print(s)

sum(100,m=1,k=1)


def intercept(list):
    if len(list)>2:
        list1 = list[0:2]
        list = list1
        return list1

list = [123,"lyh","1.23",True]
print(intercept(list))


def promitions(a,*arngs,**kwargs):
    sum = 0
    for item in arngs:
        sum += item
    print("和为{}".format(sum))
    print("a的值为",a)
    print("kwargs为",kwargs)

promitions(1,2,3,4,5,x = "lyh",y = "scy")