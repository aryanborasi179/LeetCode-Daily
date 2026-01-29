# LeetCode 3168: Minimum Number of Chairs in a Waiting Room
# Difficulty: Easy
# Topics: String
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def minimumChairs(self, s):
        count=0
        res=0
        for i in s:
            if i=="E":
                count+=1
                res=max(res,count)
            else:
                count-=1
        return res
