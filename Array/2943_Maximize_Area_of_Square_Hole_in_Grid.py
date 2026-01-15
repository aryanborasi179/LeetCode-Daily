# LeetCode 2943: Maximize Area of Square Hole in Grid
# Difficulty: Medium
# Topics: Array
# Time Complexity: O(hlogh + vlogv)
# Space Complexity: O(1)
class Solution(object):
    def longest_consecutive(self, arr):
        best_start=arr[0]
        best_len=1
        cur_start=arr[0]
        cur_len=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]+1:
                cur_len+=1
            else:
                cur_start=arr[i]
                cur_len=1
            if cur_len>best_len:
                best_len=cur_len
                best_start=cur_start
        best_end=best_start+best_len-1
        return best_start,best_end
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()
        hx,hy=self.longest_consecutive(hBars)
        vx,vy=self.longest_consecutive(vBars)
        max_len=min(hy - hx + 2, vy - vx + 2)
        return max_len**2
