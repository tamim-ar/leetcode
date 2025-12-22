class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
        for j in range(m):
            for i in range(j):
                ok = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)
        return m - max(dp)
