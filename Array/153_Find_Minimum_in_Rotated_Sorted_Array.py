# LeetCode 153: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Topics: Array
# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
