class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        idx = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        idx.sort()
        return [nums[i] for i in idx]
