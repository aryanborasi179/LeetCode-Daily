# LeetCode 3834: Merge Adjacent Equal Elements
# Difficulty: Medium
# Topics: Array
# Time Complexity: O(n²)
# Space Complexity: O(1)
class Solution(object):
    def mergeAdjacent(self, nums):
        if len(nums)==1:
            return nums
        i=1
        while i<len(nums):
            if nums[i-1]==nums[i]:
                nums[i-1]=nums[i]*2
                nums.pop(i)
                i =max(1,i-1) 
            else:
                i+=1
        return nums
