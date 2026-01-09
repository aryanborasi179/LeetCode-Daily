# LeetCode 1: Count Number of Distinct Integers After Reverse Operations
# Difficulty: Medium
# Time: O(n*k), Space: O(n)
class Solution(object):
    def countDistinctIntegers(self, nums):
        lst=[]
        lst+=nums
        for i in nums:
            tmp=str(i)
            lst.append(int(tmp[::-1]))
        lst=set(lst)
        return len(lst)
