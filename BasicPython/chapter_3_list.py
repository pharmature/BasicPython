# 在Python中，用方括号 [] 表示列表，并用逗号分隔其中的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 列表是有序集合，因此要访问列表中的任意元素，只需将该元素的位置（索引）告诉python
print(bicycles[0].title())  # 索引从0开始，而不是从1开始

# 使用列表中的元素
message = f"my favorate bicycle is {bicycles[1].title()}"
print(message)

# 修改列表元素
bicycles[0] = 'conda'
print(bicycles)

# 添加元素
# 在末尾，将 元素 附件（append()）给列表
bicycles.append('erba')
print(bicycles)

# 中间插入元素 .insert()
bicycles.insert(0, 'sanjiu')
print(bicycles)

# 删除元素
# 知道要删除的元素的位置： del
del bicycles[0]
print(bicycles)  # del 删除列表中的元素，无法再次访问

# .pop() 方法删除元素----弹出元素
# popped_bicycyle = bicycles.pop()
# print(bicycles)
# print(popped_bicycyle)

# pop() 删除列表中任意位置的元素
# popped_bicycle = bicycles.pop(1)
# print(bicycles)  # 被弹出的元素不在列表中
# print(f'my first bicycle is {popped_bicycle}.')
# 删除一个元素不再使用，选del; 删除元素后还要继续使用，选 .pop()

# 根据元素的值删除元素 .remove()
# bicycles.remove('erba')
# print(bicycles)
# remove()方法也可以继续使用删除的值
too_expensive = 'erba'
bicycles.remove(too_expensive)
print(too_expensive)
print(bicycles)
# remove()只删除第一个指定的值

# 列表排序
# 永久排序 .sort()
# bicycles.sort()
# print(bicycles)
# bicycles.sort(reverse=True)
# print(bicycles)
# 临时排序 .sorted()
print('\nhere is original list:')
print(bicycles)
print('here is sorted list:')
print(sorted(bicycles, reverse=True))
print('here is original list again:')
print(bicycles)

# 倒着打印排序 .reverse()
# print(f'\n{bicycles}')
# bicycles.reverse()
# print(bicycles)  # reverse() 不是按字母顺序反转，而是只反转列表元素的排列顺序
# reverse() 永久性地修改列表元素地顺序，但可以随时恢复顺序，只需要再次使用 reverse()

# 确定列表的长度
print(f'\n{len(bicycles)}')

# 使用列表时，注意索引是从 0 开始，而不是从 1 开始
# 访问列表的最后一个元素，可以使用索引 -1 ,列表为空是报错
print(bicycles[-1])






