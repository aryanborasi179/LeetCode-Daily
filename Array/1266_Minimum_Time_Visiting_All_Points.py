# LeetCode 1266: Minimum Time Visiting All Points
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        res=0
        for i in range(len(points)-1):
            tmp1=abs(points[i][0]-points[i+1][0])
            tmp2=abs(points[i][1]-points[i+1][1])
            if tmp1<tmp2:
                res+=tmp2
            else:
                res+=tmp1
        return res
        
