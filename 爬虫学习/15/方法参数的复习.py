# 1.必须参数
# 2.关键字参数
# 3.默认参数
# 4.可变参数

def test(*args):
    print(args)
    print(type(args))

t = (4,5,6)
test(*t)

def testdict(**parmas):
    print(parmas)
    print(type(parmas))

dict = {'name': 'ljh', 'age': 18}
testdict(**dict)
