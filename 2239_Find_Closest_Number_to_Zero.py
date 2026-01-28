# LeetCode 2239: Find Closest Number to Zero
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def findClosestNumber(self, nums):
        dict1={}
        tmp=float("inf")
        for i in nums:
            dif=abs(0-i)
            if dif not in dict1:
                dict1[dif]=[i]
            else:
                dict1[dif].append(i)
        res=max(dict1[min(dict1)])
        return res
