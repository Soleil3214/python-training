import numpy as np
 
a = np.array([[1,2],[2,4],[3,6]])
#---------------------------
# array([[1, 2],
#        [2, 4],
#        [3, 6]])
#---------------------------
 
 
# 標本分散（bias=1）
 
np.cov(a, rowvar=0, bias=1)
#-------------------------------------
# array([[ 0.66666667,  1.33333333],
#        [ 1.33333333,  2.66666667]])
#-------------------------------------
 
# 不偏分散（bias=0)

np.cov(a, rowvar=0, bias=0)
#---------------------------
# array([[ 1.,  2.],
#        [ 2.,  4.]])
#---------------------------