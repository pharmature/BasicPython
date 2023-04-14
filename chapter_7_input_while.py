# imput()函数的工作原理
# 让程序暂停运行，等待用户输入一些文本。
# 用户输入后，将其传给一个变量，方便使用
# message = input('Tell me something, and I will repeat it back to you:')
# print(message)

# 使用 int() 获取数值输入
# age = input('请输入你的年龄：')
# age = int(age)
# print(age >= 18)

# 求模运算符 %
# 两数相除并返回余数
# 判断奇数/偶数
# number = input("enter a number, and I will tell you if it's even or odd:")
# number = int(number)
# if number % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# while 循环
# num = 1
# while num < 5:
#     print(num)
#     num += 1

# 设置一个退出值
# pro = "\nTell me something and i will repeat it back to you:"
# pro += "\nenter 'quit' to end the programme:"
# message = ""
# while message != 'quit':
#     message = input(pro)
#     print(message)

# 优化
# pro = "\nTell me something and i will repeat it back to you:"
# pro += "\nenter 'quit' to end the programme:"
# message = ""
# while message != 'quit':
#     message = input(pro)
#
#     if message != 'quit':
#         print(message)


# 使用标志
# 定义一个变量，用于判断整个程序是否处在活动状态，这个变量称为标志（flag）
# pro = "\nTell me something and i will repeat it back to you:"
# pro += "\nenter 'quit' to end the programme:"
# message = ""
# active = True
# while active:
#     message = input(pro)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# break 退出循环
# prom = "\nPlease enter the name of a cite you have visited:"
# prom += "\nenter 'quit' when you are finished"
# while True:
#     city = input(prom)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd Love to go to {city.title()}")

# continue 返回循环开头，并根据条件测试结果决定是否继续执行循环
# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)

# 避免无限循环
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# ctrl + C 可以关闭显示程序输出的终端窗口

# while 循环处理列表和字典
# 在列表之间移动元素
# user_names = ['liyang', 'bao', 'zhengjie']
# confirmed_users = []
# while user_names:  # 验证每个用户，直到没有未验证用户为止
#     current_user = user_names.pop()
#
#     print(f"verifying user:{current_user.title()}!")
#     confirmed_users.append(current_user)
#
# print("\nThe following user have been confirmed:")
# for user in confirmed_users:
#     print(user.title())

# 删除特定值的所有列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\n输入姓名：")
    response = input("你的回答：")

    responses[name] = response

    repeat = input("还有人吗？(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---polling result---")
for name, response in responses.items():
    print(f"{name} like {response}!")

