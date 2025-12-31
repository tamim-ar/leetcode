class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        from collections import deque

        def can_cross(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            q = deque()
            vis = [[False]*col for _ in range(row)]
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    vis[0][j] = True

            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not vis[nx][ny] and grid[nx][ny] == 0:
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False

        l, r, ans = 0, row * col, 0
        while l <= r:
            m = (l + r) // 2
            if can_cross(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
