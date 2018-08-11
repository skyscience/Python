# 解释：
# 什么是生成器？
# 生成器算得上是Python语言中最吸引人的特性之一，生成器其实是一种特殊的迭代器，
# 不过这种迭代器更加优雅。它不需要再像上面的类一样写__iter__()
# 和__next__()方法了，只需要一个yiled关键字。

# 简单地讲，yield 的作用就是把一个函数变成一个 generator（生成器），
# 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 
# generator，带有yeild的函数遇到yeild的时候就返回一个迭代值，下次迭代时，
# 代码从 yield 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前
# 是完全一样的，于是函数继续执行，直到再次遇到 yield。

# 通俗的讲就是：在一个函数中，程序执行到yield语句的时候，程序暂停，
# 返回yield后面表达式的值，在下一次调用的时候，从yield语句暂停的
# 地方继续执行，如此循环，直到函数执行完。

# data = [i for i in range(1,100000)]
# print(data)


def gen(max):
    for i in range(1,max):
        return i
        
data = gen(10000)
print(data)
# print(type(data))
# print(next(data))
# print(next(data))

        



