class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # Every existing distinct subsequence can
            # create a new one by adding ch.
            dp[i] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD