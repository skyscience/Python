#什么是迭代器？iterator
# 那么什么迭代器呢？它是一个带状态的对象，他能在你调用next()方法
# 的时候返回容器中的下一个值，
# 任何实现了__iter__和__next__()（python2中实现next()）
# 方法的对象都是迭代器，__iter__返回迭代器自身，
# __next__返回容器中的下一个值，如果容器中没有更多元素了，
# 则抛出StopIteration异常，
# 至于它们到底是如何实现的这并不重要。

#１．它是一个类，内部有自己的实现方法　　
# ２．迭代器生成的一定是一个可以迭代的对象　　
# ３．一次性（取出来就没有了）


#什么是迭代对象？通俗的来讲：可以使用for in 来便利的对象，就是可迭代对象　（list、set、tuple）
# d = [1,2,3,4,5]
# print(next(d))

# 如何实现一个迭代器？


class students(object):
    def __init__(self):
        self.data = ['张三','王五','赵六','马云']
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result 

stus = students()

for i in stus:
    print(i)

# print(next(stus))
# print(next(stus))

