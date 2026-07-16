# 739. Daily Temperatures
# Difficulty: Medium
# Topics: Array, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans=[0]*len(temperatures)
        stack=[(0,temperatures[0])]
        for i in range(1,len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                tmp=stack.pop()
                ans[tmp[0]]=i-tmp[0]
            stack.append([i,temperatures[i]])
        return ans
