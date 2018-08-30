# import os

# def print_directory_contents(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)

a = 2
b = 3

# a = a+b
a += b
print(a)



# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)

# f(2)                  #[0,1]
# f(3,[3,2,1])      #[3,2,1,0,1,4]
# f(3)                    #[0,1,4]