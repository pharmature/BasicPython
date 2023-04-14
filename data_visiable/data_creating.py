import matplotlib
import matplotlib.pyplot as plt
# 安装matplotlib
# 导入模块pyplot,指定别名plt，包含很多用于生成图标的函数
# print(matplotlib.__version__)

# 绘制简单的折线图
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# 调用函数 subplots(), 可在一张图中绘制一个或多个图标
# 变量 fig 表示整张图片，变量 ax 表示图片中的各个图标
# ax.plot(squares)
# 调用方法 plot(), 尝试根据给定的数据以有意义的方式绘制图表

# 修改标签文字和线条粗细
# ax.plot(squares, linewidth=3)
# # 参数 linewidth 决定了plot()绘制的线条粗细
# ax.set_title("squares", fontsize=14)
# # 方法 set_title() 给图标指定标题，参数 fontsize 指定图表中各种文字的大小
# ax.set_xlabel('num', fontsize=14)
# ax.set_ylabel('num square', fontsize=14)
# # 为每条轴设置标题
# ax.tick_params(axis='both', labelsize=14)
# 设置刻度的样式，其中指定的实参将影响x轴和y轴上的刻度(axis='both'), 刻度的字号设置为14

# 校正图形
# 向 plot() 提供一系列参数时，它假设第一个数据点对应的x坐标值为0，但这里第一个对应的x值为1
# 改变这种默认行为，可以向plot()同时提供输入值和输出值
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
#
# # 使用内置样式
# plt.style.use('seaborn-darkgrid')
#
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# ax.set_title("squares", fontsize=14)
# ax.set_xlabel('num', fontsize=14)
# ax.set_ylabel('num square', fontsize=14)

# 使用scatter()绘制散点图并设置样式
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
# 设置图标的标题并给坐标轴加上标签
# ax.set_title('pingfangshu', fontsize=14)
# ax.set_xlabel('num', fontsize=14)
# ax.set_ylabel('pingfang', fontsize=14)
# # 设置刻度的大小
# ax.tick_params(axis='both', which='major', labelsize=14)


# 使用scatter()绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
#
# ax.set_title('pingfangshu', fontsize=14)
# ax.set_xlabel('num', fontsize=14)
# ax.set_ylabel('pingfang', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)

# 自动计算数据
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)  # 参数c，修改数据点的颜色
# ax.scatter(x_values, y_values, color=(1, 0.8, 0), s=10)
# 使用RGB颜色模式自定义颜色，将参数color设置为一个元组，其中包含三个0~1的小数值，分别表示红色，绿色，蓝色的分量
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)
# 颜色映射：将参数c设置成一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射
ax.set_title('pingfangshu', fontsize=14)
ax.set_xlabel('num', fontsize=14)
ax.set_ylabel('pingfang', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])  # 设置每个坐标轴的取值范围

# plt.show()
# 函数 plt.show() 打开matplotlib查看器并显示绘制的图标
plt.savefig('squares_plot.png', bbox_inches='tight')
# 自动将图表保存到文件中
# 第一个实参指定要以什么文件名保存图标，这个文件将存储到.py文件所在的目录
# 第二个实参指定将多余的空白区域裁剪掉，如果要保留空白，只需省略这个实参






