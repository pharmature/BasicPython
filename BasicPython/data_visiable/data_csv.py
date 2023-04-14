# CSV文件格式：一系列以逗号分隔的值
# 分析CSV文件头
import csv
import matplotlib.pyplot as plt


filename = 'bc_data.csv'
f = open(filename)
reader = csv.reader(f)
# 调用csv.reader()将存储的文件对象作为实参传递，从而创建一个与该文件相关联的阅读器对象
header_row = next(reader)
# 模块csv包含函数next()，返回文件中的下一行。
# 只调用了一次next()，因此得到的是文件的第一行，其中包含头文件
# print(header_row)

# 打印文件头机器位置
# for index, column_header in enumerate(header_row):
#     # 函数enumerate()获取每个元素的索引及其值
#     print(index, column_header)

# 提取并读取数据
# highs = []
# for row in reader:  # 遍历余下的各行
#     # 阅读器对象从其停留的地方继续向下读取csv文件，每次都自动返回当前所处位置的下一行
#     # 每次执行循环时，都将索引6处的数据附加到highs末尾
#     high = float(row[6])
#     highs.append(high)

# print(highs)

# 绘制图表
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs, c='red')
#
# ax.set_title('0000', fontsize=14)
# ax.set_xlabel('', fontsize=14)
# ax.set_ylabel('smoothness_mean', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=16)

# 模块datetime添加日期
# 将"2018-7-1"转换为一个表示相应日期的方法，可使用datetime中的方法strptime()
# 方法strptime()可接受各种实参，并根据他们来决定如何解读日期
# %A-星期几(Monday) %B-月份名(January) %m-用数表示的月份 %d-用数表示的月份的一天
# %Y-四位的年份 %y-两位的年份 %H-24小时制的小时数 %I-12小时制的小时数 %p-am或pm %M-分钟数 %S-秒数
# from datetime import datetime
# first_date = datetime.strptime('2018-7-1', '%Y-%m-%d')
# print(first_date)

# 再绘制一个数据系列
ids = range(569)
highs = []
lows = []
for row in reader:
    low = float(row[6])
    lows.append(low)
    high = float(row[2])
    highs.append(high)

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(ids, highs, c='blue', alpha=0.5)
ax.plot(ids, lows, c='red', alpha=0.5)  # 实参alpha指定颜色的透明度，0完全透明，1完全不透明

# 给图表区域着色
ax.fill_between(ids, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('000', fontsize=14)
ax.set_xlabel('id', fontsize=14)
ax.set_ylabel('num', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()



