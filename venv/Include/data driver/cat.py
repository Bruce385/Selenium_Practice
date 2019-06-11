
class Cat:
    # 创建init方法      参数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 对init方法调用
    def __str__(self):
        return "%s的年龄%d岁" % (self.name, self.age)
    # 创建方法
    def sing(self):
        print("猫在唱歌")
    def dance(self):
        print("猫在跳舞")
# 创建对象
tom = Cat("老王的猫", 40)
# 调用对象中的方法
tom.sing()
tom.dance()
print(tom)