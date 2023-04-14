import matplotlib
import matplotlib.pyplot as plt
# 安装matplotlib
# 导入模块pyplot,指定别名plt，包含很多用于生成图标的函数
print(matplotlib.__version__)

# 绘制简单的折线图
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# 调用函数 subplots(), 可在一张图中绘制一个或多个图表
# 变量 fig 表示整张图片，变量 ax 表示图片中的各个图表
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
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("squares", fontsize=14)
ax.set_xlabel('num', fontsize=14)
ax.set_ylabel('num square', fontsize=14)


plt.show()
# 函数 plt.show() 打开matplotlib查看器并显示绘制的图标

