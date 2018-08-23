from numpy import *
import numpy as np

a1=array([1,2,3])
a1=mat(a1)

#1print(a1)  [[1 2 3]]
#
a1=mat([[1,1],[2,3],[4,2]]);
#2print(a1)  [[1 1]
#			 [2 3]
#			 [4 2]]
		 
#3print(a1[1,:])	 [[2 3]]
	 
#4print(sum(a1[1,:]))  计算第一行所有列的和  5

#print(a1[1:])   [[2 3]
#				  [4 2]]

#print(a1[1:,1:])	分割出第二行以后的行和第二列以后的列的所有元素	
#[[3]
# [2]]
