# 函数调用
import Basic.loop

# 自动售卖功能
def drink_machine(money,*drink_type):
    total = 0
    map = {"橙汁":3.5,"椰汁":4,"矿泉水":2,"早餐奶":4.5}
    for i in range(len(drink_type)):
        if drink_type[i] in map:
            # 计算总金额
            total += float(map[drink_type[i]])
        else:
            return "未找到您要买的饮料"
    # 判断金额
    if isinstance(money,int):
        if total < float(money):
            change = money - total
            return "您购买的饮料为{}，找零{}".format(drink_type, change)
        elif total > float(money):
            return "订单总金额{},您已支付{},还需支付{}".format(total,money,total - money)
        else:
            return "购买成功"
    else:
        return money
# 投币功能
def coin(*cash):
    money = 0
    for i in range(len(cash)):
        if int(cash[i]) in (1,5,10):
            money += int(cash[i])
        else:
            return "投币失败，当前只支持（1,5,10）面值硬币或纸币"
    return money


print(drink_machine(coin(1,5),"橙汁","早餐奶"))