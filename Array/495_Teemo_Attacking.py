# LeetCode 495: Teemo Attacking
# Difficulty: Easy
# Topics: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        res=0
        for i in range(len(timeSeries)-1):
            tmp=timeSeries[i]+duration
            res+=duration
            if tmp>=timeSeries[i+1]:
                res-=(tmp-timeSeries[i+1])
        res+=duration
        return res
