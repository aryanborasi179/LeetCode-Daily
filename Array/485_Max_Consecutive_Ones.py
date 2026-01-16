# LeetCode 485: Max Consecutive Ones
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                if count>res:
                    res=count
            else:
                count=0
        return res
