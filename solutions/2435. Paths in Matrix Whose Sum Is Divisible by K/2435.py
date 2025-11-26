class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(m):
            for j in range(n):
                r = grid[i][j] % k
                if i > 0:
                    for x in range(k):
                        dp[i][j][(x + r) % k] = (dp[i][j][(x + r) % k] + dp[i-1][j][x]) % mod
                if j > 0:
                    for x in range(k):
                        dp[i][j][(x + r) % k] = (dp[i][j][(x + r) % k] + dp[i][j-1][x]) % mod
                        
        return dp[m-1][n-1][0]
