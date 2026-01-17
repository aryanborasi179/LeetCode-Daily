# LeetCode 14: Longest Common Prefix
# Difficulty: Easy
# Topics: Array, String
# Time Complexity: O(n * m)
# Space Complexity: O(m)
class Solution(object):
    def longestCommonPrefix(self, strs):
        res=""
        for i in range(len(strs[0])):
            tmp=True
            for j in strs:
                if i<=len(j)-1:
                    if strs[0][i]!=j[i]:
                        tmp=False
                else:
                    return res
            if tmp==True:
                res+=strs[0][i]
            else:
                return res
        return res
