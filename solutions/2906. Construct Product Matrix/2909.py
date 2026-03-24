class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Step 1: Flatten
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Step 2: Prefix products
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Step 3: Suffix products
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Step 4: Result array
        res = [0] * size
        for i in range(size):
            res[i] = (prefix[i] * suffix[i]) % MOD
        
        # Step 5: Convert back to 2D
        idx = 0
        for i in range(n):
            for j in range(m):
                grid[i][j] = res[idx]
                idx += 1
        
        return grid