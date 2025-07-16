from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if (nums[i] + nums[j]) % 2 == (nums[j] + nums[j-1]) % 2 if j > 0 else True:
                    dp[i][(nums[i] + nums[j]) % 2] = max(dp[i][(nums[i] + nums[j]) % 2], dp[j][(nums[j] + nums[j-1]) % 2 if j > 0 else (nums[i] + nums[j]) % 2] + 1)
        return max(max(row) for row in dp)
