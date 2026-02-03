# LeetCode 3637: Trionic Array I
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def isTrionic(self, nums):
        i=0
        while i<len(nums)-1 and nums[i]<nums[i+1]:
            i+=1
        if i==0 or i==len(nums)-1:
            return False
        while i<len(nums)-1 and nums[i]>nums[i+1]:
            i+=1
        if i==len(nums)-1:
            return False
        while i<len(nums)-1:
            if nums[i]>=nums[i+1]:
                return False
            i+=1
        return True
