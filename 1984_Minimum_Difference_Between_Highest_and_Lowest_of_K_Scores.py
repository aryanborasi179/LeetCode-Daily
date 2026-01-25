# LeetCode 1984. Minimum Difference Between Highest and Lowest of K Scores
# Difficulty: Easy
# Topics: Array, Sliding window
# Time Complexity: O(n log n)
# Space Complexity: O(1)
class Solution(object):
    def minimumDifference(self, nums, k):
        if k==1:
            return 0
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-k+1):
                res=min(res,nums[i+k-1]-nums[i])    
        return res
