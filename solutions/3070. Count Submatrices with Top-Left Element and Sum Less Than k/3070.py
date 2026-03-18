class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # build prefix sum
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                
                # check condition
                if grid[i][j] <= k:
                    count += 1
        
        return count