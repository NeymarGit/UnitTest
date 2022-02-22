userInfo = {"admin": "123321", "user1": "123456"}
count = 3
status = False
while True:
    if count == 0:
        print("您输错密码次数过多，请30分钟后重试")
        break
    if status:
        break
    else:
        name = input("请输入用户名：")
        if name in userInfo.keys():
            while count > 0:
                pwd = input("请输入密码：")
                if pwd == userInfo[name]:
                    print("登录成功")
                    status = True
                    break
                else:
                    count -= 1
                    if count > 0:
                        print("密码输入错误，您还有{}次机会".format(count))
                        continue
                    else:
                        break
            # break
        else:
            continue
