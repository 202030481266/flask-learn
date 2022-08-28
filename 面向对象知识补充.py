from time import sleep
import json
import re
import logging

# 设置日志格式
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

# 创建类的两种方式
'''
class A(object):

    CITY = "beijing"

    def func(x):
        return x + 1


B = type('B', (object,), {'CITY':'shanghai', 'func': lambda x: x + 1})


def main():
    oo1 = A
    oo2 = B
    print(oo1.func(2))
    print(oo2.func(3))


if __name__ == "__main__":
    main()
'''
# 如果继承的类由某一个指定的metaclass创建，那么类也是通过指定的metaclass创建
'''
class MyType(type):

    def __init__(self, *args, **kwargs):
        print('create class')
        super().__init__(*args,**kwargs)
        print('finish create')

class Foo(object,metaclass=MyType):

    CITY = 'BJ'

    def func(self,x):
        return x + 1

class xxx(Foo):
    pass

create class
finish create
create class
finish create
'''