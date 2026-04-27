class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        from collections import deque
        q = deque([(0, 0)])
        vis = {(0, 0)}

        while q:
            x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis:
                    if (-dx, -dy) in dirs[grid[nx][ny]]:
                        vis.add((nx, ny))
                        q.append((nx, ny))

        return False