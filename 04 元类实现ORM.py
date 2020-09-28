# __author__:"Ming Luo"
# date:2020/9/28

# ORM 是 python编程语言后端web框架 Django的核心思想，
# “Object Relational Mapping”，即对象-关系映射，简称ORM。


# 说明
# 1. 所谓的ORM就是让开发者在操作数据库的时候，能够像操作对象时通过xxxx.属性=yyyy一样简单，这是开发ORM的初衷
# 2. 只不过ORM的实现较为复杂，Django中已经实现了 很复杂的操作，
# 本节知识 主要通过完成一个 insert相类似的ORM，理解其中的道理就就可以了
# 简单输入  --->  sql 语句

# 定义元类
# 将类属性值变为字典__mappings__
# 定义类属性__table__
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            # 在此简单起见，采用元组传入，即判断是否是元组
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # python不支持在对某个字典进行遍历的时候对其对其大小进行修改
        for i in mappings:
            del attrs[i]

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()
        for temp in args:
            # 判断入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)

class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
# print("对应的sql语句")
u.save()
