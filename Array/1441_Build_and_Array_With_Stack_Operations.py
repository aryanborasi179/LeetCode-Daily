# LeetCode 1441. Build an Array With Stack Operations
# Difficulty: Medium
# Topics: Array, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def buildArray(self, target, n):
        s=set(target)
        result=[]
        for i in range(1,n+1):
            if i not in s:
                result.append("Push")
                result.append("Pop")
            else:
                result.append("Push")
            if i==target[-1]:
                break
        return result        
