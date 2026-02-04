# 1.常见数据类型

# python中常见的基础数据类型
# int - 整形：存放整数
# float - 浮点型：存放小数
# str - 字符串：用引号引起来的都是字符串
# bool - 布尔类型：True、False
# NoneType - 空值：仅包含None

# 通过type()语句来得到数据的类型
print(type("hello python"))
print(type(10))
print(type(3.14))

# 变量本身是没有类型的，type(变量)输出的类型是变量中存储的数据的类型
num = 5.0
print(type(num))

# 通过isinstance()检查数据是否属于指定的类型，返回的是一个bool值
print(isinstance(num, int))
print(isinstance(num, float))


# 2.字符串

# 字符串的三种定义方式
# (1)双引号定义
str1 = "hello"
# (2)单引号定义
str2 = 'python'
# (3)三引号定义（多行字符串）
str3 = """
hello:
    c
    c++
    python
"""

# 字符：是文本世界的基本单位，一个字母、一个数字、一个标点符号、一个汉字等都是一个字符

# 转义字符
# 常见的转义字符
# \' - 单引号
# \" - 双引号
# \n - 换行符
# \t - 制表符
str4 = 'It\'s very interesting'
print(type(str4))
# 或者交替使用单引号、双引号
str5 = "It's very interesting"
print(type(str5))


# 3.字符串拼接
# 多个字符串字面量直接写，python解释器会自动拼接
slogan1 = "python " "is very interesting."
print(slogan1)
# + 号拼接
slogan2 = "python " + "is very interesting."
print(slogan2)
# 多个部分拼接
s1 = "人生苦短"
s2 = "我用python"
print("python is interesting." + s1 + "," + s2)
# +号可以用来拼接两个字符串，但是无妨将非字符串与字符串进行拼接
# 非字符串类型需要转换为字符串类型

# str() - 将数据类型转为字符串
age = 18
print("今年" + str(age) + "岁")


# 4.字符串格式化

# 通过 %占位符 的形式完成字符串和变量的快速拼接
# % 表示我要占位，s 表示将变量转为字符串放入占位的位置
str6 = "python"
str7 = "nihao"
print("hello %s %s" %(str6, str7))

# 通过 f"内容{变量/表达式}" 的形式完成快速格式化 - 推荐
print(f"hello {str6}, {str7}")






