# LeetCode 3274. Check if Two Chessboard Squares Have the Same Color
# Difficulty: Easy
# Topics: Math
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        dict1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        color_1=dict1[coordinate1[0]]+int(coordinate1[1])
        color_2=dict1[coordinate2[0]]+int(coordinate2[1])
        return (color_1%2)==(color_2%2)
