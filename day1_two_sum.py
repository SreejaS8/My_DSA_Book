#two sum
class Solution:
    def twoSum(self, n, t):
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i]+n[j] == t:
                    print(i,j)

solution = Solution()            
solution.twoSum([3,4,5,6,7,8,9], 12)