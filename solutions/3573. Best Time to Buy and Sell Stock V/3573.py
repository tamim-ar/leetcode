class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -10**18

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, end_state):
            if j < 0:
                return NEG
            if i < 0:
                return 0 if end_state == 0 else NEG
            p = prices[i]
            if end_state == 0:
                return max(
                    dfs(i - 1, j, 0),
                    dfs(i - 1, j, 1) + p,
                    dfs(i - 1, j, 2) - p
                )
            if end_state == 1:
                return max(
                    dfs(i - 1, j, 1),
                    dfs(i - 1, j - 1, 0) - p
                )
            return max(
                dfs(i - 1, j, 2),
                dfs(i - 1, j - 1, 0) + p
            )

        return dfs(n - 1, k, 0)
