# 对象
class Animal:
    hava_meat = True

    def __init__(self,name="lyh",age=23):
        self.name = name
        self.age = age

    # 实例方法
    def move(self):
        print("{}{}动物都会跑".format(self.name,self.age))
        self.eat("海鲜")

    def eat(self,*a):
        print("动物都会吃{}".format(a))

    # 类方法
    @classmethod
    def swimming(cls):
        print("会游泳")

    # 静态方法
    @staticmethod
    def dance():
        print("会跳舞")


human = Animal()
human.move()
print(human.hava_meat)


# 类方法和静态方法可以直接通过类名.方法名调用，且不能直接调用类的属性
Animal.swimming()
Animal.dance()
