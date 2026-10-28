class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                val = set()
                if i == 0 and j == 0: val.add(0)
                if i > 0: val.update(dp[j])
                if j > 0: val.update(dp[j - 1])
                dp[j] = {v ^ grid[i][j] for v in val}
        return min(dp[-1])