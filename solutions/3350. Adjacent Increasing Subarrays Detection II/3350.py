class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        res = 0
        for i in range(1, n):
            res = max(res, min(inc[i], inc[i - 1]))
        return res
