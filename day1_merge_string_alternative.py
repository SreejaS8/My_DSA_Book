#Merge strings alternatively 
## input : s1 = "abc", s2 = "pqr"
## output : "apbqcr"

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ''
        for i in range(max(len(word1), len(word2))):
            try:
                s += word1[i]
            except IndexError:
                s += ''
            try:
                s += word2[i]
            except IndexError:
                s += ''
        return s
    
word1 = str(input())
word2 = str(input())
p = Solution().mergeAlternately(word1,word2)
print(p)