# 字典  {a: 1, b: 2, c: 3, ......}

# 字典是一系列 键值对 ，每个键都有一个值相关联，可以用键来访问相关联的值
# 与键相关的值可以是 数、字符串、列表、字典

# 访问字典中的值
# alien_0 = {'color': 'green', 'points': 5}
# new_point = alien_0['points']
# print(f"you just earned {new_point} points!")

# 添加键值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# 先创建一个空字典
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
#
# # 修改字典中的值
# alien_0['color'] = 'red'
# print(alien_0)
#
# # 删除键值对
# # del 彻底删除相应的键值对
# del alien_0['color']
# print(alien_0)  # 键值对永久消失

# 由类似对象组成的字典
# favorate_languages = {
#     'jens': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',  # 加逗号，为以后在下一行添加键值对做好准备
#     }
#
# language = favorate_languages['sarah'].title()
# print(f"Sarah's favorate language is {language}.")

# 使用 get() 来访问值
# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0[points])  # 显示traceback错误
# point_value = alien_0.get('points', 'no point value assinged')
# point_value = alien_0.get('points')
#
# # 第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的
# print(point_value)

# 遍历字典
# 遍历所有键值对
# user_0 = {'username': 'efermi',
#           'first': 'enrico',
#           'lase': 'fermi'}
# for key, value in user_0.items():  # 声明两个变量，存储键值对中的键和值，可以用任意名称
#     print(f'\nkey:{key}')
#     print(f'value:{value}')

# 遍历字典中的所有键
favorate_languages = {
    'jens': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # 加逗号，为以后在下一行添加键值对做好准备
    }
# for name in favorate_languages.keys():
# # .key() 可以省略，即 for name in favorate_languages:
#     print(name.title())


# friends = ['jens', 'sarah']
# for name in favorate_languages:
#     print(f"Hi,{name}")
#
#     if name in friends:
#         language = favorate_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
#
# if 'erin' not in favorate_languages.keys():  # keys() 并非只能用于遍历，它返回一个列表，其中包含字典中所有的键
#     print("Erin, please take our poll!")
#
# languages = favorate_languages.keys()
# print(languages)

# 按特定顺序返回元素 .sorted()
# for name in sorted(favorate_languages.keys()):
#     print(f"{name.title()},Thank you for taking the poll")

# 遍历字典中的所有值
# for language in favorate_languages.values():
#     print(language.title())
# .values() 没有考虑是否重复

# 为剔除重复项，可使用集合 set()， 集合中的每个元素必须独一无二
# 集合 {'python', 'C', 'Javascript'}  容易与字典混淆，都是用花括号定义
# 但是字典没有冒号，即没有键值对，与列表和字典不同，集合不会以特定的顺序存储元素
# for language in set(favorate_languages.values()):
#     print(language)
# 得到不重复的列表

# 嵌套
# 字典列表
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'red', 'points': 10}
# alien_2 = {'color': 'blue', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# range()函数创建30个外星人
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# print(f"Total number of aliens: {len(aliens)}")

# 在字典中存储字典
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }

for user_name, user_ifo in users.items():
    print(f'\nusername:{user_name}')
    full_name = f"{user_ifo['first']} {user_ifo['last']}"
    location = user_ifo['location']

    print(full_name)
    print(location)




