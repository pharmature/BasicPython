# 随机漫步：每次行走都是随机的、没有明确的，结果是由一系列随机决策决定的
# 可以将随机漫步看作蚂蚁再晕头转向的情况下，每次都沿随机的方向前行所经过的路径

# 创建RandomWalk类
from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):  # 初始化随机漫步的属性
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

# 选择方向,使用方法fill_walk()来生成漫步包含的点并决定每次漫步的方向
    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            # choice给x_direction选择一个值
            x_distance = choice([0, 1, 2, 3, 4])
            # choice随机选择一个0~4的整数
            x_step = x_direction *x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)





