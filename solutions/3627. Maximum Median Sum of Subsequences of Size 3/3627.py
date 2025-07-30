class Solution:
    def maximumMedianSum(self, nums):
        nums.sort()
        n = len(nums)
        k = n // 3
        return sum(nums[i] for i in range(n - 2, k - 1, -2))
