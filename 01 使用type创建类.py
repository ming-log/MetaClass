# __author__:"Ming Luo"
# date:2020/9/28
# type具有两种功能
# 1. type(object)   -> the object's type
type(3)    # -> int
type(0.5)  # -> float

# 2. type(object_or_name, bases, dict)    -> a new type
# object_or_name: 类名
# bases:父类   如果无可以省略，或者写
# dict:属性、方法构成的字典
# 添加的属性是类属性，并不是实例属性
Test = type("Test", (), {"num": 100, "num2": 0.111})
help(Test)
test = Test()
test.num
test.num2


# 3. 利用type创建带有方法的类
def func1(self):
    print(self.num)


@staticmethod  # 添加静态方法
def func2():
    print("静态方法!")
    return "静态方法返回值"


@classmethod    # 添加类方法
def func3(cls):
    print(cls.func2())
    print("类方法!")


Test2 = type("Test2", (Test, ), {"func1": func1, "func2": func2, "func3": func3})
test2 = Test2()
test2.func1()
test2.func2()
test2.func3()
