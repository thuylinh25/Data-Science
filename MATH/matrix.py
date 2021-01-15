import numpy as np
# tính ma trận đảo nghịch inverse matrix
# A = np.array([[1,-3,0,0],
#               [0,1,-3,0],
#               [0,0,1,-3],
#               [0,0,0,1]])
# print(np.linalg.inv(A))
# tính định thức determinant (det)
A = np.array([[1,2,-1,4],
              [-1,-1,3,5],
              [2,-1,-3,3],
              [1,1,1,5]])
#
print(np.linalg.det(A))
# mat1 = ([2,1],
#         [-3,1])
# mat2 = ([-1,1],
#         [0,1])
# res = np.dot(mat1,mat2)
# print(res)
#
# A = np.array([[1,-2,-1,2],
#               [-1,-1,3,2],
#               [2,-1,-3,1],
#               [1,1,1,4]])
# print(np.linalg.matrix_rank(A))