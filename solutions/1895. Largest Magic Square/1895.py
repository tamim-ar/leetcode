from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        d1 = [[0]*(n+1) for _ in range(m+1)]
        d2 = [[0]*(n+2) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                d1[i+1][j+1] = d1[i][j] + grid[i][j]
                d2[i+1][j] = d2[i][j+1] + grid[i][j]

        def rowsum(i, j, k):
            return row[i][j+k] - row[i][j]

        def colsum(i, j, k):
            return col[i+k][j] - col[i][j]

        def diag1(i, j, k):
            return d1[i+k][j+k] - d1[i][j]

        def diag2(i, j, k):
            return d2[i+k][j] - d2[i][j+k]

        ans = 1
        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    s = rowsum(i, j, k)
                    if diag1(i, j, k) != s or diag2(i, j, k) != s:
                        continue
                    ok = True
                    for x in range(k):
                        if rowsum(i + x, j, k) != s or colsum(i, j + x, k) != s:
                            ok = False
                            break
                    if ok:
                        ans = k
        return ans
