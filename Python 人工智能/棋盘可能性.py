# 3     3+3x2 = 9      
# 4     4+4x3+4x3x2=40
# 5     5+5x4+5x4x3+5x4x3x2=205


# a+a*(a-1)
# a+a*(a-1)+a*(a-1)*(a-2)
# a+a*(a-1)+a*(a-1)*(a-2)+a*(a-1)*(a-2)*(a-3)


# 4     4+4x3+4x3x2=40
# a = 4
# a*(a-1) = 12
# a*(a-1)*(a-2) = 24


a = int(input('请输入棋盘格子数'))
b = 0
for i in range(1,a):
    c = a
    for j in range(1,i):
        c *= a-j
    b += c
print('B: ',b)
