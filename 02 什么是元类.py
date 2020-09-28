# __author__:"Ming Luo"
# date:2020/9/28

# 元类就是类的类
# 函数type实际上是一个元类。
# type就是Python在背后用来创建所有类的元类
# 通过检查__class__属性来看到这一点。
# Python中所有的东西，注意，我是指所有的东西——都是对象。
# 这包括整数、字符串、函数以及类。
# 它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type。
a = 35
a.__class__
a.__class__.__class__
b = "35"
b.__class__
b.__class__.__class__
c = (35, 35)
c.__class__
c.__class__.__class__
d = [35, 35]
d.__class__
d.__class__.__class__
e = {"a": 35}
e.__class__
e.__class__.__class__
def f(): pass
f.__class__
f.__class__.__class__
class g: pass
g.__class__
g.__class__.__class__
