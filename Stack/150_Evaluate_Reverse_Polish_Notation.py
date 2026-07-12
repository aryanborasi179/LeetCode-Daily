# 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
# Topics: Array, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for i in tokens:
            if i in {"+","-","*","/"}:
                a=stack.pop()
                b=stack.pop()
                if i=="*":
                    stack.append(a*b)
                elif i=="+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(b-a)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(i))
        return stack[-1]
        
