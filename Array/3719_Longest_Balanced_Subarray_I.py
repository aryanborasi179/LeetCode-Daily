# LeetCode 3719: Longest Balanced Subarray I
# Difficulty: Medium
# Topics: Array
# Time Complexity: O(n²)
# Space Complexity: O(n)
class Solution(object):
    def longestBalanced(self, nums):
        res=0
        n = len(nums)
        for i in range(n):
            odd=set()
            even=set()
            for j in range(i, n):
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even)==len(odd):
                    res=max(res,j - i + 1)
        return res
        
