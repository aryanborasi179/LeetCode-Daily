# LeetCode 1877: Minimize Maximum Pair Sum in Array
# Difficulty: Medium
# Topics: Array, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)
class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        res=0
        for i in range(len(nums)//2):
            tmp=(nums[i]+nums[-(i+1)])
            res=max(tmp,res)
        return res
