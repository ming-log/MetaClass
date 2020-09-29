# __author__:"Ming Luo"
# date:2020/9/28


# 原始类
class fun(object):
    age = 18
    gender = "男"


# 假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。
# 如何通过元类来实现
def upper_all_attr(class_name, class_parent, class_attr):
    for k, v in class_attr.items():
        if not k.startswith("__"):
            del class_attr[k]
            class_attr[k.upper()] = v
    return type(class_name, class_parent, class_attr)


class func1(object, metaclass=upper_all_attr):  # metaclass：指定元类， 默认为type
    age = 18
    gender = "男"


# 真正的class来当做元类。
class upper_attr(type):
    def __new__(cls, class_name, class_parent, class_attr):
        for k, v in class_attr.items():
            if not k.startswith("__"):
                del class_attr[k]
                class_attr[k.upper()] = v
        return type(class_name, class_parent, class_attr)


class func2(object, metaclass=upper_attr):
    age = 18
    gender = "男"


# 采用type重写
def __new__(cls, class_name, class_parent, class_attr):
    print(class_attr)
    for k, v in class_attr.items():
        if not k.startswith("__"):
            del class_attr[k]
            class_attr[k.upper()] = v
    print(class_attr)
    return type(class_name, class_parent, class_attr)


upper_attr = type("upper_attr", (type, ), {"__new__": __new__})


class func3(object, metaclass=upper_attr):
    age = 18
    gender = "男"

# 就元类本身而言，它们其实是很简单的：
# 1. 拦截类的创建
# 2. 修改类
# 3. 返回修改之后的类
