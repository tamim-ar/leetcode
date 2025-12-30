class Solution:
    def numMagicSquaresInside(self, grid):
        r, c = len(grid), len(grid[0])
        res = 0

        def is_magic(i, j):
            nums = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            s = sum(grid[i][j:j+3])
            for x in range(3):
                if sum(grid[i+x][j:j+3]) != s:
                    return False
                if sum(grid[i+k][j+x] for k in range(3)) != s:
                    return False
            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != s:
                return False
            if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != s:
                return False
            return True

        for i in range(r - 2):
            for j in range(c - 2):
                if is_magic(i, j):
                    res += 1

        return res
