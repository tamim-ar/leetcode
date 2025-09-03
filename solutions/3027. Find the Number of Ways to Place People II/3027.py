from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        xs = sorted(set(p[0] for p in points))
        ys = sorted(set(p[1] for p in points))
        
        xi = {x:i for i,x in enumerate(xs)}
        yi = {y:i for i,y in enumerate(ys)}
        n = len(points)
        grid = [[0]*len(ys) for _ in range(len(xs))]
        
        for x, y in points:
            grid[xi[x]][yi[y]] = 1
        
        # prefix sum
        ps = [[0]*(len(ys)+1) for _ in range(len(xs)+1)]
        for i in range(len(xs)):
            for j in range(len(ys)):
                ps[i+1][j+1] = grid[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
        
        def query(x1, y1, x2, y2):
            return ps[x2+1][y2+1] - ps[x1][y2+1] - ps[x2+1][y1] + ps[x1][y1]
        
        ans = 0
        for i in range(n):
            ax, ay = points[i]
            for j in range(n):
                if i == j:
                    continue
                bx, by = points[j]
                if bx < ax or by > ay:
                    continue
                x1, y1 = xi[ax], yi[by]
                x2, y2 = xi[bx], yi[ay]
                if query(x1, y1, x2, y2) == 2:
                    ans += 1
        return ans
