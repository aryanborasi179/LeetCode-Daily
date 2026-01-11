# LeetCode 1561: Maximum Number of Coins You Can Get
# Difficulty: Medium
# Topics: Array
# Approach:
#   - Greedy
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        k=(len(piles)//3)*2
        res=0
        for i in range(1,k+1,2):
            res+=piles[i]
        return res
