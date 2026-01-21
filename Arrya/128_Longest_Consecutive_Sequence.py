# LeetCode 128: Longest Consecutive Sequence
# Difficulty: Medium
# Topics: Array, Hash-table
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        res=0
        for i in nums:
            if i-1 not in nums:
                count=1
                curr=i
                while curr+1 in nums:
                    curr+=1
                    count+=1
                res=max(count,res)
        return res
