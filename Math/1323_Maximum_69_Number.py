# LeetCode 1323: Maximum 69 Number
# Difficulty: Easy
# Topics: Math
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def maximum69Number (self, num):
        num=str(num)
        res=""
        tmp=True
        for i in num:
            if i=="6" and tmp:
                res+="9"
                tmp=False
            else:
                res+=i
        return int(res)
