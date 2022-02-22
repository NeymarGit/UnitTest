price = input("请输入商品价格：")
if price.isdigit():
    price = int(price)
    if price >= 50 and price <= 100:
        discount = "9折"
        total = price * 0.9
    elif price > 100:
        discount = "8折"
        total = price * 0.8
    else:
        discount = "无折扣"
        total = price
    print("商品折扣为：{0}，折后总价为：{1:.2f}".format(discount, total))
else:
    print("请输入正确的价格!!")


# import random
#
# a = random.randint(1,9)
# print(a)
# b = int(input("请输入数字："))
# if a < b:
#     print("bigger")
# elif a > b:
#     print("less")
# else:
#     print("equal")
