from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c, steps = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    if nr in (0, rows - 1) or nc in (0, cols - 1):
                        return steps + 1
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))
        
        return -1
