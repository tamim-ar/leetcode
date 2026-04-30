from typing import List
import heapq

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                for cost in range(k+1):
                    if dp[i][j][cost] == -1:
                        continue
                    
                    for di, dj in [(0,1),(1,0)]:
                        ni, nj = i+di, j+dj
                        if ni < m and nj < n:
                            val = grid[ni][nj]
                            new_cost = cost + (1 if val > 0 else 0)
                            if new_cost <= k:
                                dp[ni][nj][new_cost] = max(
                                    dp[ni][nj][new_cost],
                                    dp[i][j][cost] + val
                                )
        
        res = max(dp[m-1][n-1])
        return res if res != -1 else -1