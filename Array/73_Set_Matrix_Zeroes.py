# LeetCode 73: Set Matrix Zeroes
# Difficulty: Medium
# Topics: Array, Matrix
# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
class Solution(object):
    def setZeroes(self, matrix):
        set_i=set()
        set_j=set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    set_i.add(i)
                    set_j.add(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if i in set_i or j in set_j:
                    matrix[i][j]=0
        return matrix
