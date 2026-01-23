# LeetCode 441: Arranging Coins
# Difficulty: Easy
# Topics: Math
# Time Complexity: O(√n)
# Space Complexity: O(1)
class Solution(object):
    def arrangeCoins(self, n):
        i=1
        count=0
        while True:
            count+=1
            n-=i
            if n==0:
                return count
            if n<0:
                return count-1
            i+=1
        
