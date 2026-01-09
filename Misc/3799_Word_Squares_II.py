# LeetCode 3799: Word Squares II
# Difficulty: Medium
# Topic: (Array, String, Sorting)
# Time Complexity: O(N!)
# Space Complexity: O(N!)
from itertools import permutations
class Solution(object):
    def wordSquares(self, words):
        res=list(permutations(words,4))
        result=[]
        for i in res:
            top=i[0]
            left=i[1]
            right=i[2]
            bottom=i[3]
            if top[0]==left[0] and top[3]==right[0] and bottom[0]==left[3] and bottom[3]==right[3]:
                result.append(list(i))
        return sorted(result)
