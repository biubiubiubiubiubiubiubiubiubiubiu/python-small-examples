# 测试函数执行时间的装饰器示例

import time


def timing_func(fn):
    def wrapper():
        start = time.time()
        fn()  # 执行传入的fn参数
        stop = time.time()
        return (stop-start)
    return wrapper


@timing_func
def test_list_append():
    lst = []
    for i in range(0, int(1e6)):
        lst.append(i)


@timing_func
def test_list_compre():
    [i for i in range(0, int(1e6))]  # 列表生成式


a = test_list_append()
c = test_list_compre()
print("test list append time:", a)
print("test list comprehension time:", c)
print("append/compre:", round(a/c, 3))
# @timing_func修饰test_list_append意味着完成两步操作，
# 将test_list_append作为timing_func()的参数即执行timing_func(test_list_append),
# 然后将test_list_append替换成timing_func()返回的结果。
# 即被修饰的函数总是被替换成@符号所引用的函数返回值。
