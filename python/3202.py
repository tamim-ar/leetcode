from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 1

        for j in range(n):
            for i in range(j):
                mod = (nums[i] + nums[j]) % k
                dp[j][mod] = max(dp[j][mod], dp[i][mod] + 1)
                ans = max(ans, dp[j][mod] + 1)

        return ans
