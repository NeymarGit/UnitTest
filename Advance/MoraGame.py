import random


# 猜拳游戏

class MoraGame:
    role_dirt = {1: "曹操", 2: "张飞", 3: "刘备"}
    mora_dirt = {1: "剪刀", 2: "石头", 3: "布"}

    # 选择角色
    def choose_role(self):
        role = input("请选择角色（1:曹操,2:张飞,3:刘备）：")
        return role

    def player_choose_mora(self):
        player_mora = input("请选择出拳（1:剪刀,2:石头,3:布）：")
        return player_mora

    def computer_mora(self):
        computer_mora = random.randint(1, 3)
        return computer_mora

    def mora_vs(self):
        role = int(self.choose_role())
        player_win = 0
        computer_win = 0
        draw = 0

        while True:
            player_mora = int(self.player_choose_mora())
            print("{}出拳为{}".format(self.role_dirt[role], self.mora_dirt[player_mora]))
            computer_mora = self.computer_mora()
            print("电脑出拳为{}".format(self.mora_dirt[computer_mora]))
            if player_mora == computer_mora:
                draw += 1
                print("这局为平局")
            elif (player_mora == 1 and computer_mora == 2) or (player_mora == 2 and computer_mora == 3) or (
                    player_mora == 3 and computer_mora == 1):
                computer_win += 1
                print("这局为电脑赢")
            else:
                player_win += 1
                print("这局为{}赢".format(self.role_dirt[role]))
            is_continue = input("是否继续猜拳？（按Y继续，按N退出）")
            if is_continue == "Y":
                continue
            elif is_continue == "N":
                break
        print("您一共赢了{}局，电脑一共赢了{}局，{}局平局".format(player_win, computer_win, draw))


mg = MoraGame()
mg.mora_vs()
