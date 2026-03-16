class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        s = set()

        for r in range(m):
            for c in range(n):
                s.add(grid[r][c])

                k = 1
                while r-k >= 0 and r+k < m and c-k >= 0 and c+k < n:
                    total = 0

                    x, y = r-k, c

                    for _ in range(k):
                        total += grid[x][y]
                        x += 1
                        y += 1

                    for _ in range(k):
                        total += grid[x][y]
                        x += 1
                        y -= 1

                    for _ in range(k):
                        total += grid[x][y]
                        x -= 1
                        y -= 1

                    for _ in range(k):
                        total += grid[x][y]
                        x -= 1
                        y += 1

                    s.add(total)
                    k += 1

        return sorted(s, reverse=True)[:3]