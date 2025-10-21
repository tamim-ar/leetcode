class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        l = 0
        res = 1
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, min(r - l + 1, numOperations + 1))
        return res
