class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0
        for i in range(2, n + 1):
            share = (share + dp[i - delay] - dp[i - forget]) % mod
            dp[i] = share
        return sum(dp[n - forget + 1: n + 1]) % mod
