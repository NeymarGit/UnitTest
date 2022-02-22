
class MathParent:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("父类的加法",self.a + self.b)

    def sub(self):
        print(self.a - self.b)


class MathChild(MathParent):
    def mul(self):
        print(self.a * self.b)

    def add(self):
        super(MathChild,self).add()
        print("子类的加法",self.a + self.b+10)


mc = MathChild(3,2)
mc.add()