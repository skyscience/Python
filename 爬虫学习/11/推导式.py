#
# 推导式comprehensions（又称解析式），是Python的一种独有特性。
# 推导式是可以从一个数据序列构建另一个新的数据序列的结构体。
# 共有三种推导，在Python2和3中都有支持：

# 列表(list)推导式
l_a = [1,2,3,4,5,6,7,8]
# la_t = []
# for i in l_a:
#     i = i*i
#     la_t.append(i)
l_a_t = [i*i for i in [i*i for i in l_a] if i > 16 ]
print(l_a_t)

# 字典(dict)推导式
d_class = {
    '201':40,
    '203':20,
    '205':100,
}
d_class_t = {key:value for key,value in d_class.items() if value>20}
print(type(d_class_t))
print(d_class_t)
# for key,value in d_class.items():


# 集合(set)推导式
s_d = {1,2,3,4,5,6}
s_d_t = {i+1 for i in s_d if i > 1}
print(type(s_d_t))
print(s_d_t)

#有没有元组推导式？？？？？？
tup_d = (1,2,3,4,5,6)
tup_d_t = (i-2 for i in tup_d if i > 2)
print(type(tup_d_t))
print(tup_d_t)






