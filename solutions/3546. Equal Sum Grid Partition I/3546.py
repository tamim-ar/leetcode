from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total sum is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # 1. Check horizontal cuts
        curr = 0
        for i in range(m - 1):  # cut must leave both parts non-empty
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # 2. Check vertical cuts
        col_sum = [0] * n
        for j in range(n):
            for i in range(m):
                col_sum[j] += grid[i][j]
        
        curr = 0
        for j in range(n - 1):
            curr += col_sum[j]
            if curr == target:
                return True
        
        return False