class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1

    def get_descriptive(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it!")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:  # 定义一个新类，没有继承任何类
    def __init__(self, battery_size=75):  # 初始化电池的属性
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery!")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):  # 创建子类
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


