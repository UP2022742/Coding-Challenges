# Given an n x n matrix where each of the rows and columns are sorted in 
# ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth 
# distinct element.

""" First Example
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13

Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and 
the 8th smallest number is 13
"""

""" Second Example
Input: matrix = [[-5]], k = 1
Output: -5    
"""

# Contstraints:
# 1. n == matrix.length
# 2. n == matrix[i].length
# 3. 1 <= n <= 300
# 4. -109 <= matrix[i][j] <= 109
# 5. All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 6. 1 <= k <= n2

def kthSmallest(matrix, k):

    # Flattens array, sorts it then returns the index - 1.
    return sorted([j for sub in matrix for j in sub])[k-1]

print(kthSmallest(matrix=[[-5]], k=1))