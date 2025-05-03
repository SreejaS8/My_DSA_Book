class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        r = set()
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                n = nums[i]+nums[j]+nums[k]
                if n == 0:
                    r.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif n < 0:
                    j += 1
                else:
                    k -= 1
        a = list(r)
        return a
                
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
p = Solution().threeSum(nums)
print(p)