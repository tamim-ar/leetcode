from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefix_sum = [0] * (k + 1)
        prefix_hash = [0] * (k + 1)

        for i in range(k):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]
            prefix_hash[i + 1] = (prefix_hash[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)

            if L == R:
                ans.append(0)
                continue

            total_sum = prefix_sum[R] - prefix_sum[L]

            x = (
                prefix_hash[R]
                - prefix_hash[L] * pow10[R - L]
            ) % MOD

            ans.append((x * total_sum) % MOD)

        return ans