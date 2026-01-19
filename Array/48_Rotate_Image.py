# LeetCode 48: Rotate Image
# Difficulty: Medium
# Topics: Array, Math, Matrix
# Time Complexity: O(n²)
# Space Complexity: O(n²)
class Solution(object):
    def rotate(self, matrix):
        lst=[]
        for l in range(len(matrix)):
            lst.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                lst[j].append(matrix[i][j])
        for k in range(len(lst)):
            lst[k].reverse()
        matrix[:]=lst
