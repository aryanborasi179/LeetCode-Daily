# LeetCode 1481: Least Number of Unique Integers after K Removals
# Difficulty: Medium
# Topics: Array, sorting, Hash table
# Approach:
#   - Greedy
# Time Complexity: O(n + ulogu)
# Space Complexity: O(u)
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        arr=Counter(arr)
        lst=[]
        for i in arr:
            lst.append(arr[i])
        lst.sort()
        j=0
        while k>0:
            if k>lst[j]:
                k-=lst[j]
                lst[j]=0
            else:
                lst[j]=lst[j]-k
                k=0
            j+=1
        count=0
        for ele in lst:
            if ele>0:
                count+=1
        return count
