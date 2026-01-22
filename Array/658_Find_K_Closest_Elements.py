# LeetCode 658. Find K Closest Elements
# Difficulty: Medium
# Topics: Array, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        lst=[]
        for i in range(len(arr)):
            lst.append((arr[i],abs(arr[i]-x)))
        lst.sort(key=lambda x:x[1])
        res=[]
        for j in range(k):
            res.append(lst[j][0])
        return sorted(res)
        
