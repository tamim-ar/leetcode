
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        # Create a unique path: right across the first row,
        # then down the last column.
        for j in range(n):
            grid[0][j] = '.'

        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]
