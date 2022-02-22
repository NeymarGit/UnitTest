import datetime

class Tickets:
    def __init__(self,date,*info):
        self.date = date
        self.info = info;

    def price(self):
        price = 100
        # 获取星期几
        week_day = datetime.datetime.strptime(self.date,"%Y-%m-%d").weekday()
        if week_day in (5,6):
            return price*1.2
        else:
            return price

    def get_total(self):
        total_child = 0
        total_adult = 0
        for item in self.info:
            if int(item) <= 12:
                total_child += self.price() * 0.5
            else:
                total_adult += self.price()
        return total_adult + total_child

family_1 = Tickets("2021-07-17",10,12,32,35)
print(family_1.get_total())

