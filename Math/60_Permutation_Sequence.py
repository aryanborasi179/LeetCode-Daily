# LeetCode 60. Permutation Sequence
# Difficulty: Hard
# Topics: Math
# Time Complexity: O(n * n!)
# Space Complexity: O(n * n!)
from itertools import permutations
class Solution(object):
    def getPermutation(self, n, k):
        string=""
        for i in range(1,n+1):
            string+=str(i)
        lst=[]
        for j in permutations(string):
            lst.append(''.join(j))
        return lst[k-1]
        
