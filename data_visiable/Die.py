from random import randint
# 创建Die类
class Die:
    def __init__(self, num_size=6):
        # 骰子默认为6面
        self.num_size = num_size

    def roll(self):
        # 返回一个位于1和骰子面数之间的随机值,包括初始值1和终止值num_size
        return randint(1, self.num_size)






