from plotly.graph_objs import Bar, Layout
from plotly import offline

from Die import Die

D6 = Die()

# 将结果存储在列表中
results = []

for roll_num in range(1000):
    result = D6.roll()
    results.append(result)
# print(results)

# 分析结果
frequencies = []
for value in range(1, D6.num_size+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 绘制直方图
x_values = list(range(1, D6.num_size+1))
# 将可能出现的点数存储在一个名为x_values的列表中
# plotly 不能直接接受函数range()的结果，因此需要使用函数list()将其转换为列表
data = [Bar(x=x_values, y=frequencies)]
# Plotly 类Bar()表示用于绘制条形图的数据集
# 需要一个存储x值的列表和一个存储y值的列表。这个类必须放在方括号内，因为数据集可能包含多个元素

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
# 每个坐标轴都能以不同的方式进行配置，而每个配置选项都是一个字典元素。这里只设置了坐标轴标签

my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# 类Layout()返回一个指定图表布局和配置的对象。设置图表名，并传入x轴和y轴的配置字典
offline.plot({'data': data, 'layout': my_layout}, filename='D6.html')
# 函数offline.plot()，需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里


# 同时投掷两个骰子
D6_1 = Die()
D6_2 = Die()

results = []
for roll_num in range(1000):
    result = D6_1.roll() + D6_2.roll()
    results.append(result)


frequencies = []
max_result = D6_1.num_size + D6_2.num_size
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
# dtick键指定了x轴显示的刻度间距；'dtick': 1让plotly显示每个刻度值
y_axis_config = {'title': '结果的频率'}

my_layout = Layout(title='掷两个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6_D6.html')


# 同时掷两个不同面数的骰子
D6 = Die()
D10 = Die(10)

results = []
for roll_num in range(5000):
    result = D6.roll() + D10.roll()
    results.append(result)

frequencies = []
max_result = D6.num_size + D10.num_size
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '频率'}
my_layout = Layout(title='掷一个D6和一个D10 5000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6_D10.html')




