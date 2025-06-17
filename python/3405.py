MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n, m, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = m

        for i in range(2, n + 1):
            for j in range(k + 1):
                dp[i][j] += dp[i - 1][j] * (m - 1)
                dp[i][j] %= MOD
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] %= MOD

        return dp[n][k]
