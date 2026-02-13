# LeetCode 3227. Vowels Game in a String
# Difficulty: Medium
# Topics: String
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def doesAliceWin(self, s):
        vowel=0
        for i in s:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                vowel+=1
        if vowel==0:
            return False
        return True
