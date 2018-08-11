# 要求
# 0 0\ 0
# 0 1\ 1
# 1 0\ 1
# 1 1\ 0

a = int(input('请输入第1个'))
b = int(input('请输入第2个'))
# OR
if a or b:
    if a:
        if b:
            print('假')
        else:
            print('真')
    else:
        print('真')
else:
    print('假')



# AND
if a and b:
    if a:
        if b:
            print('假')
        else:
            print('真')
    else:
        print('真')
else:
    if a or b:
        print('真')
    else:
        print('假')