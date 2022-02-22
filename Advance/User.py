class User:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self)

    def greet_user(self):
        print("{}岁时由{}更改名为{}".format(self.age,self.first_name,self.last_name))

user_one = User("小二","小九",10)
user_one.describe_user()
user_one.greet_user()

user_two = User("小云","小白",18)
user_two.describe_user()
user_two.greet_user()