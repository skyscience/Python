import numpy as np
z=np.array([
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
	])
print(z.reshape(2,-1,4,1))
print(z.shape[0])
