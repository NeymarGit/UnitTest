# 反射

class Data:
    data = "lyh"

if __name__ == '__main__':

    print(getattr(Data,"data")) # 获取类里的属性
    setattr(Data,"data","wsc") # 修改类里的属性
    print(Data.data)
    print(hasattr(Data,"data")) # 判断属性是否存在
    delattr(Data,"data") # 删除类的属性
    print(hasattr(Data,"data")) # 判断属性是否存在

