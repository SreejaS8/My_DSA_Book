#Merge strings alternatively 
## input : s1 = "abc", s2 = "pqr"
## output : "apbqcr"

class Solution(object):
    def mergeAlternatively(self, s1, s2):
        if(s1>s2):
            m = s1
        else:
            m = s2
        s = ""
        for i in range(len(m)):
            s = s+s1[i]+s2[i]
        print(s)
solution = Solution()
s1 = str(input("s1: "))
s2 = str(input("s2: "))
solution.mergeAlternatively(s1, s2)