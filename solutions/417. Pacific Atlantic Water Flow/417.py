from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or r >= m or c < 0 or c >= n 
                or (r, c) in visited 
                or heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        pacific, atlantic = set(), set()
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        return list(pacific & atlantic)
