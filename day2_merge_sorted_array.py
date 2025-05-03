class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m):
            nums1[m+i] = nums2[i]
        nums1.sort()

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
p = solution.merge(nums1, m, nums2, n)
print(p)