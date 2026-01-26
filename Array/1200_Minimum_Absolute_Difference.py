# LeetCode 1200. Minimum Absolute Difference
# Difficulty: Easy
# Topics: Array, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution(object):
    def minimumAbsDifference(self, arr):
        dict1={}
        arr.sort()
        for i in range(len(arr)-1):
            dif=abs(arr[i]-arr[i+1])
            if dif not in dict1:
                dict1[dif]=[[arr[i],arr[i+1]]]
            else:
                dict1[dif].append([arr[i],arr[i+1]])
        return dict1[min(dict1)]
