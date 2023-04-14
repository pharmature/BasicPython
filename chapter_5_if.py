# 条件语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

# 检查是否相等
# for car in cars:
#     if car == 'audi':
#         print(car.upper())
#
#     if car == 'bmw':
#         print(car.title())

# 在python中检查是否相等时区分大小写，大小写不同的值被视为不相等

# 检查是否不相等
# requested_topping = 'mushroom'
# if requested_topping != 'anchovies':
#     print("hold the fire!")

# 数值比较
# age = 18
# if age == 18:
#     print("成年")
# 条件语句中可包含各种数学比较：小于<, 大于, 小于等于, 大于等于

# 检查多个条件
# 使用 and
# age = 18
# weight = 75
# if age == 18 and weight ==75:
#     print('he is the one!')

# 使用 or
# if age >= 25 or weight >= 25:
#     print('yes!!')

# 检查特定值是否包含在列表中
# numbers = [1, 2, 3, 4, 5, 6]
# if 3 in numbers:
#     print('true')
# 检查特定值是否不包含在列表中
# if 7 not in numbers:
#     print('false')


# 布尔表达式  bool函数
# 结果为 True 或 False


# if 语句
'''
if condition1:
    do thing_1
    
elif condition2:
    do thing_2
.
.
.
else:
    do thing_n
'''

# 使用if语句处理列表

# 检查特殊元素
# requested_toppings = ['liyang', 'baochuang', 'zhengjie', 'panpan']
# for num in requested_toppings:
#     if num == 'liyang':
#         print('he is the first')
#     else:
#         print('others')

# 确定列表不是空的
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"adding{requested_topping}")
#     print('\nyou have finished your pizza')
#
# else:
#     print('are you sure you want a plan pizza?')

# 使用多个列表
# requested_toppings = ['liyang', 'baochuang', 'zhengjie', 'panpan']
# available_toppings = ['liyang', 'baochuang', 'zhengjie']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"finding:{requested_topping}")
#
#     else:
#         print(f"not finding:{requested_topping}")






