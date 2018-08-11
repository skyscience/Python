
# 列表(list)推导式
l_a = [1, 2, 3, 4, 5, 6, 7, 8]

#+1 +3 +5 +7 +8
# l_a_t = []
# for i in l_a:
#     i = i*i
#     l_a_t.append(i)

# 第二种方法
l_a_t = [i*i for i in [i*i for i in l_a] if i > 16]
print(l_a_t)
