# LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution(object):
    def minimumCost(self, nums):
        res=nums[0]
        lst=nums[1:]
        lst.sort()
        res+=lst[0]
        res+=lst[1]
        return res
