# LeetCode 135: Candy
# Difficulty: Hard
# Topics: Array, Greedy
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def candy(self, ratings):
        res=[]
        tmp=0
        if len(ratings)>1:
            if ratings[0]>ratings[1]:
                tmp=2
                res.append(tmp)
            else:
                tmp=1
                res.append(tmp)
        else:
            return 1
        for i in range(1,len(ratings)):
            if ratings[i]<=ratings[i-1]:
                tmp=1
                res.append(tmp)
            else:
                tmp+=1
                res.append(tmp)
        for j in range(len(res)-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                if res[j]<=res[j+1]:
                    res[j]=res[j+1]+1
        return sum(res)
        
