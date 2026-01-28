# LeetCode 384: Shuffle an Array
# Difficulty: Medium
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):

    def __init__(self, nums):
        self.original=nums[:]
        self.nums=nums[:]

    def reset(self):
        self.nums=self.original[:]
        return self.nums

    def shuffle(self):
        lst=self.nums[:]
        random.shuffle(lst)
        return lst
