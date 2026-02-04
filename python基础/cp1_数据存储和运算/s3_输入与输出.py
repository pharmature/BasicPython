# 1.输入
# input语句(函数)的功能就是获取键盘输入的数据
# 具体用法 s = input(提示信息)
from PyQt5.QtSql import password

# print语句(函数)的功能就是将数据输出到控制台
# 具体用法 print(数据)

name = input("please input your name:")
age = input("please input your age:")
print(f"your name is {name} and your age is {age}")

# 无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型

# 案例：银行卡ATM取款
# 总金额
total = 10000
# 输入密码
passwords = input("please input your password:")
print(f"密码正确 {passwords}")
# 输入取款金额
num = input("请输入取款金额")
# 计算余额并输出 - int() 转为int类型
print(f"取款后银行卡余额为{total - int(num)}")




