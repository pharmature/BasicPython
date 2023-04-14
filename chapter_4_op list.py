# 遍历列表
magicians = ['liyang', 'Baochuang', 'zhengjie']
# for magician in magicians:
#     print(magician)
#
# for magician in magicians:
#     print(f'{magician.title()},that is a great trick.')
#     print(f"I can't wait to see your next trick,{magician.title()}.\n")
#
# print('thank you, everyone!That was a great magic show.')

# 避免缩进错误
# 忘记缩进
# for magician in magicians:
# print(magician)
# 忘记缩进额外的代码行
# for magician in magicians:
#     print(f'{magician.title()},that is a great trick.')
# print(f"I can't wait to see your next trick,{magician.title()}.\n")
# 不必要的缩进
# message = "Hello Python world!"
#     print(message)
# 循环后不必要的缩进
# for magician in magicians:
#     print(f'{magician.title()},that is a great trick.')
#     print(f"I can't wait to see your next trick,{magician.title()}.\n")
#
#     print('thank you, everyone!That was a great magic show.\n')
# 遗漏了冒号

# 创建数值列表
# range() 函数
# for value in range(1, 5):
#     print(value)
# print('\n')
# for value in range(5):
#     print(value)

# 使用range()函数创建数字列表
# numbers = list(range(5))
# print(numbers)
# # 可以指定步长
# numbers = list(range(1, 10, 2))
# print(numbers)

# range()函数几乎可以创建任何需要的数集
# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
# print(squares)
#
# for value in range(2, 12):
#     squares.append(value**2)
# print(squares)

# 数字列表简单的计算,最大值，最小值，总和
# numbers = [1, 2, 5, 9, 3, 6]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 列表解析
# squares = [value**2 for value in range(1, 5)]  # 没有冒号
# print(squares)

# 使用列表的一部分
players = ['Liyang', 'Baochuang', 'Zhengjie', 'lengsang', 'panpan']
# 切片
# print(players[0:3])
# print(players[1:4])  # 生成列表的任意子集
# print(players[:4])  # 从列表的第一个元素开始
# print(players[1:])  # 到列表的末尾结束
# print(players[-2:])  # 负数索引返回离列表末尾相应距离的元素

# 遍历切片
# print('here is my players:')
# for player in players[:3]:
#     print(player.title())

# 复制列表
# my_players = players[:]
# #my_players = players 表达是错误的，这是将players赋给my_players,而不是它的副本
# print(my_players)

# 元组
# 创建一系列不能更改的元素，不可变的列表叫做 元组
# dimensions = (1, 2, 3, 5, 9, 4)
# print(dimensions[0])
# print(dimensions[3])

# 尝试修改
# dimensions[0] = 10
# print(dimensions)

# 遍历元组中的所有值
# for dimension in dimensions:
#     print(dimension)

# 修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
# dimensions = (4, 5)
# print('original dimensions:')
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (6, 7)
# print('\nmodified dimensions:')
# for dimension in dimensions:
#     print(dimension)


# 设置代码格式
# 格式设置指南  PEP8
# 缩进 常用制表符 \t
# 行长 建议每行不超过80个字符
# 空行 将程序的不同部分分开，只影响代码的可读性





