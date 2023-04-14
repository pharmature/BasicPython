# 定义函数
# def 函数名():
#     函数体
# 函数调用，直接输入函数名
# def green_name():
#     print("5555")
#
#
# green_name()  # 函数前后留两行空格

# 向函数传递信息
# def greet_user(username):
#     print(f"Hello,{username.title()}")
#
#
# greet_user('liyang')
# 形参和实参
# username 是一个形参，即函数完成工作需要的信息
# 'liyang' 是一个实参，即调用函数时传递给函数的信息

# 传递实参
# 位置实参：调用函数时，python 必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 最简单的关联方式时基于实参的顺序，这种关联方式称为位置实参
# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
#
#
# describe_pet('dog', 'zhengjie')
# describe_pet('cat', 'liyang')  # 多次调用函数
# 位置实参的顺序非常重要

# 关键字实参
# 关键字实参时传递给函数的名称值对。
# 因为直接在实参中将名称和值关联起来，所以向函数传递参数时不会混淆
# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet(animal_type='dog', pet_name='liyang')
# 关键字实参的顺序无关紧要，因为python知道各个值该赋给哪个形参

# 默认值
# 编写函数时，可以给每个形参指定默认值，调用函数时给形参提供了实参，python将使用指定的是参数值，否则，将使用形参的默认值
# def describe_pet(pet_name, animal_type='dog'):
#     # 注意，修改了形参的排列顺序，因为给animal_type指定了默认值，无需通过实参来指定动物类型，所以在函数调用中值包含了一个实参
#     # python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.\n")


# 等效的函数调用
# describe_pet(pet_name='willie')
# describe_pet('willie')
# describe_pet(pet_name='harry', animal_type='hamster')

# 避免实参错误
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.\n")


# describe_pet()  # 缺少必要的实参


# 返回值
# 函数并非总是直接显示输出，还可以处理一些数据，并返回一个或一组值，函数返回的值称为返回值
# 在函数中，可使用 return 语句将值返回到调用函数的代码行
# 返回简单值
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('liyang', 'zhengjie')
# print(musician)


# 让实参变成可选的
# 使用函数的人就能只在必要时提供额外的信息
# 可给形参 middle_name 指定一个空的默认值，并在用户没有提供中间名时不使用这个形参
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('liyang', 'zhengjie')
# print(musician)
# musician = get_formatted_name('liyang', 'baochuang', 'zhengjie')
# print(musician)

# 返回字典
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
#
#
# musician = build_person('liyang', 'zhengjie')
# print(musician)
# 扩展函数
# def build_person(first_name, last_name, age=None):  # None 相当于 False, 视为占位值
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('liyang', 'zhengjie',age=27)
# print(musician)

# 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello,{formatted_name}")


# 定义退出条件
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("enter 'q' at any time to quit.")
#
#     f_name = input("First name:")
#     if f_name == 'q':
#         break
#     l_name = input("Last name:")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello,{formatted_name}")

# 传递列表
# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
#
#
# usernames = ['liyang', 'baochuan', 'zhengjie']
# greet_users(usernames)

# 在函数中修改列表

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model:{current_design.title()}")
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print(f"The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []


# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# 禁止修改函数列表
# print_models(unprinted_designs[:], completed_models)  # 切片表示法 [:] 创建列表的副本
# print(unprinted_designs)

# 传递任意数量的实参
# def make_pizza(*topping):
#     # 形参名 *topping 中的星号让python创建一个名为topping的空元组，并将所有收集到的值都封装到这个元组中
#     print(*topping)
#
#
# make_pizza('pepp')
# make_pizza('mushroom', 'green pepp', 'cheese')

# 将函数调用print（）替换为一个循环，遍历
# def make_pizza(*toppings):
#     print(f"\nMaking a pizza with the following toppings")
#     for topping in toppings:
#         print(f"-{topping}")
#
#
# make_pizza('pepp')
# make_pizza('mushroom', 'green pepp', 'cheese')


# 结合位置实参和任意数量实参
# def make_pizza(size, *toppings):
#     print(f"Making a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
#
#
# make_pizza(5, 'pepp')
# make_pizza(5, 'mushroom', 'green pepp', 'cheese')
# 通用形参名 *args 收集任意数量的实参位置


# 使用任意数量的关键字实参
# def build_profile(first, last, **user_ifo):
#     # 先创建一个字典，其中包含我们知道的有关用户的一切
#     # 形参 **user_ifo 中的两个星号让python创建一个名为user_ifo 的空字典，并将收到的所有名称值对都放在这个字典中
#     user_ifo['first_name'] = first
#     user_ifo['last_name'] = last
#     return user_ifo
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
# 形参 **kwargs 收集任意数量的关键字实参

# 将函数存储在模块中
# 可将代码块与主程序分离，将函数储存在称为模块的独立文件中，再将模块导入到主程序中
# import 语句允许在当前运行的程序文件中使用模块的代码
# 将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序
# import pizza
# pizza.make_pizza(5, 'pess')
# pizza.make_pizza(12, 'mushroon', 'green pepp', 'cheese')

# 导入特定的函数
# from pizza import make_pizza
# make_pizza(16, 'pes')
# make_pizza(12, 'mush', 'gre', 'cheese')

# 使用 as 给函数指定别名
# from pizza import make_pizza as mp
# mp(12, 'pes')
# mp(16, 'mush', 'gre', 'cheese')

# 使用 as 给模块指定别名
# import pizza as p
# p.make_pizza(12, 'pes')
# p.make_pizza(16, 'mus', 'gre', 'che')

# 导入函数中的所有函数
# from pizza import *
# make_pizza(16, 'pes')
# make_pizza(12, 'mush', 'gre', 'cheese')

# 函数编写指南
# 给函数指定描述性名称，且只在其中使用小写字母和下划线，可帮助你和别人明白代码想要做什么，模块的命名也遵循
#













