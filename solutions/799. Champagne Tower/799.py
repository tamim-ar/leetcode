class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[r][c] = কতটা champagne এসে জমেছে (cap=1.0 এর আগে)
        dp = [[0.0] * (query_row + 2) for _ in range(query_row + 2)]
        dp[0][0] = float(poured)

        for r in range(query_row + 1):
            for c in range(r + 1):
                overflow = max(0.0, dp[r][c] - 1.0)
                if overflow > 0:
                    dp[r + 1][c] += overflow / 2.0
                    dp[r + 1][c + 1] += overflow / 2.0

        return min(1.0, dp[query_row][query_glass])
