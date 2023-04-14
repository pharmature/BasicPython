# 创建和使用类
# 创建Dog 类
# class Dog:  # 根据约定，在python中，首字母大写的是类；类的定义中没有括号，因为要从空白创建这个类
#     def __init__(self, name, age):
        # __init__()方法：类中的函数称为方法，调用的方法与调用函数不同
        # 特殊方法，每次创建实例时，会自动运行
        # 开头和末尾各有两条下划线，这是一种约定，旨在避免python默认方法与普通方法发生名称冲突
        # 三个形参：self必不可少，而且必须位于其他形参的前面，python调用这个方法来创建Dog类时，将会自动传入实参self，指向实例本身的引用
        # self自动传递，不需要传递它，因此根据Dog类创建实例时，都会给后两个形参name和age提供值
        # self.name = name
        # self.age = age
    #     以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问
    # self.name = name 获取与形参name相关联的值，并将其赋给变量name,然后该变量被关联到当前创建的实例
    # self.age = age 类似
    # 像这样可通过实例访问的变量称为 属性。

    # def sit(self):
    #     print(f"{self.name} is now sitting!")
    #
    # def roll_over(self):
    #     print(f"{self.name} rolled over")


# 根据类创建实例
# my_dog = Dog('willie', 6)
# 访问属性
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog's age is {my_dog.age}")
# 调用方法
# my_dog.sit()
# my_dog.roll_over()
# 创建多个实例
# 可按需求根据类创建任意数量的实例


# 使用类和实例
# car类
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive())


# 给属性指定默认值
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1
#     # 创建一个odometer_reading属性，并将其初始值设置为1
#
#     def get_descriptive(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it!")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive())
# my_new_car.read_odometer()
#
# # 修改属性的值
# # 直接修改属性的值
# my_new_car.odometer_reading = 12
# my_new_car.read_odometer()
#
# # 通过方法修改属性的值
# my_new_car.update_odometer(20)
# my_new_car.read_odometer()
#
# # 通过方法对属性的值进行递增
# my_new_car.increment_odometer(20)
# my_new_car.read_odometer()


# 继承
# 编写类时，并非总是要从空白开始，如果要编写的类是另一个现成类的特殊版本，可以使用继承
# 一个类继承另一个类时，将自动获得另一个类的所有属性和方法
# 原有的类称为父类，新的类称为子类
# 子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法

# 子类的方法 __init__()
# 在既有类的基础上编写新类时，通常要调用父类的方法__init__，这将初始化父类__init__()方法中定义的所有属性，从而让子类包含这些属性

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1
#     # 创建一个odometer_reading属性，并将其初始值设置为1
#
#     def get_descriptive(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it!")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):  # 创建子类
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)  # __init__()方法接受创建Car实例所需的信息
# #       super()是个特殊的函数，让你能够调用父类的函数
# #       父类因此也被称为 超类。
#         self.battery_size = 75
#
#     def describe_battery(self):
#         print(f"battery size:{self.battery_size}")
#
#     def increment_odometer(self):
#         self.odometer_reading += 10


# my_Tesla = ElectricCar('audi', 'a4', 2019)
# print(my_Tesla.get_descriptive())

# 给子类定义属性和方法
# my_Tesla.describe_battery()

# 重写父类的方法
# 在子类中定义一个与要重写的父类方法同名的方法
# my_Tesla.increment_odometer()
# my_Tesla.read_odometer()


# 将实例用作属性
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1
#
#     def get_descriptive(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it!")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery:  # 定义一个新类，没有继承任何类
#     def __init__(self, battery_size=75):  # 初始化电池的属性
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kwh battery!")
#
#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} miles on a full charge.")
#
#
# class ElectricCar(Car):  # 创建子类
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()  # python创建一个新的Battery 实例，并将该实例赋给属性self.battery
#
#
# my_Tesla = ElectricCar('audi', 'a4', 2019)
#
# print(my_Tesla.get_descriptive())
# my_Tesla.battery.describe_battery()
# my_Tesla.battery.get_range()


# 导入类
# 导入单个类
# from Car import Car
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 在一个模块中存储多个类
# 从一个模块中导入多个类
from Car import Car, ElectricCar

# 导入整个模块
import Car

# 导入模块中的所有类
from Car import *
# 不推荐使用
# 一，只看开头的import语句，就能清楚知道程序使用了哪些类，但这种导入方式没有明确指出使用了模块中的哪些类
# 二，可能引发名称方面的疑惑

# 在一个模块中导入另一个模块
from car_1 import Car
from electric_car import ElectricCar

# 使用别名
from electric_car import ElectricCar as EC

# python 标准库
# 一组模块，安装的python都包含
# random 模块中
# randint() 函数，将两个整数作为参数，并随机返回一个位于这两数之间（含）的整数
# choice() 函数，将一个列表或元组作为参数，随机返回其中一个元素

# 类编码风格
# 类名采用驼峰命名法，将类名中的每个单词的首字母大写，而不使用下划线
# 实例名和模块名都采用小写格式，并在单词之间加下划线
# 使用空行来组织代码，在类中，一个空行来分隔方法，模块中，两个空行来分隔类
# 同时导入标准库中的模块和自己编写的模块时，先导入标准库模块
# 再添加一个空行，然后导入自己编写的库；更容易理解程序使用的各个模块都来自何处


