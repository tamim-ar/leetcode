class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        
        res = f
        
        for i in range(n - 1, 0, -1):
            f = f + total - n * nums[i]
            res = max(res, f)
        
        return res