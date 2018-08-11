# 例1 阶乘 4x3x2x1 = 24
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1


# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num + 1):  #循环次数 = 输入的次数
        factorial = factorial*i
        # 1 = 1x1
        # 1 = 1x2
        # 2 = 2x3
        # 6 = 6x4
    print("%d 的阶乘为 %d" % (num, factorial))