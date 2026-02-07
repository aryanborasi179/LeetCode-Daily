# LeetCode 1556: Thousand Separator
# Difficulty: Easy
# Topics: String
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def thousandSeparator(self, n):
        n=str(n)
        if len(n)<4:
            return n
        n=n[::-1]
        res=""
        count=0
        for i in n:
            if count!=0 and count%3==0:
                res+="."
            count+=1
            res+=i
        return res[::-1]
        
