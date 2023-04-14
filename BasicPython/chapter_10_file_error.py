# 从文件中读取数据
# 读取整个文件
# 首先创建文件
# 然后读取文件
# 1.打开文件, 是文件从硬盘中存到内存中
# open(file, mode= 'r', encoding=None)
# file 要操作的文件名字，类型是 str
# mode, 文件打开的方式 r(read) 只读打开, w(write) 只写打开, a(append) 追加打开
# encoding 文件的编码格式，常见的编码格式有两种，一种是gbk, 一种是utf-8
# 返回值, 文件对象，后续所有的文件操作，都需要通过这个文件对象进行
f = open('pi_digit.txt', 'r')
# 2.读写文件
buf = f.read()
print(buf)
# 输出的末尾多了一个空行，因为read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来就是一个空行
# 删除空行
print(buf.rstrip())
# 3.关闭文件  文件.close()  将内存当中的文件同步到硬盘中


with open('pi_digit.txt') as file_object:
    contents = file_object.read()

print(contents)


# 文件路径
# 相对文件路径
# with open('txt_file/pi_digit.txt') as file_object：
# 绝对文件路径
# file_path = '/home/ehmatthes/other_files/text_files/pi_digit.txt'
# with open(file_path) as file_object:

# 逐行读取

