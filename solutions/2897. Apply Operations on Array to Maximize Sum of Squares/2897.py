
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30

        # Count how many numbers contain each bit
        for num in nums:
            for b in range(30):
                if num & (1 << b):
                    cnt[b] += 1

        ans = 0

        # Construct k numbers greedily
        for _ in range(k):
            x = 0
            for b in range(30):
                if cnt[b] > 0:
                    x |= 1 << b
                    cnt[b] -= 1

            ans = (ans + x * x) % MOD

        return ans
