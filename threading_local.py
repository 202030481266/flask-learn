from threading import local, Thread, get_ident
from time import sleep

xianglong = local()

# def task(arg):
#     xianglong.value = arg
#     sleep(1)
#     print(xianglong.value)

storage = {}

# 使用字典实现
def set(k, v):
    ident = get_ident()
    if ident in storage:
        storage[ident][k] = v
    else:
        storage[ident] = {k : v}


def get(k):
    ident = get_ident()
    return storage[ident][k]


def task(arg):
    set('val', arg)
    sleep(2)
    v = get('val')
    print(v)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()


# 封装的版本
class Local(object):

    def __init__(self):
        # self.storage = dict() 会出现问题因为会无限调用 __setattr__ 方法
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k : v}

    def __getattr__(self, k):
        ident = get_ident()
        return self.storage[ident][k]























