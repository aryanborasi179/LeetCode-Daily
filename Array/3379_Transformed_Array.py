# LeetCode 3379: Transformed Array
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def constructTransformedArray(self, nums):
        result=[]
        for i in range(len(nums)):
            if nums[i]==0:
                result.append(0)
            else:
                tmp=(i+nums[i])%len(nums)
                result.append(nums[tmp])
        return result
