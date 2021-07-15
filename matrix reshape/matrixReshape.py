# In MATLAB, there is a handy function called reshape which can reshape an m x n 
# matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the 
# number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original 
# matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output 
# the new reshaped matrix; Otherwise, output the original matrix.

""" First Example
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""

""" Second Example
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

# Constraints:
# 1. m == mat.length
# 2. n == mat[i].length
# 3. 1 <= m, n <= 100
# 4. -1000 <= mat[i][j] <= 1000
# 5. 1 <= r, c <= 300

import math
def matrixReshape(mat, r, c):

    # Difference between each iteration.
    if r < c: split_value = c
    else: split_value = r

    # Flatten the array.
    flatMatrix = [j for sub in mat for j in sub]

    # Return comp
    return [flatMatrix[index : index+split_value] for index in range(0, len(flatMatrix), split_value)]

print(matrixReshape([[1,2],[3,4]],2,2))

#########################
# TODO: INCOMPLETE      #
#########################