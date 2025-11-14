class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0]*(n+1) for _ in range(n+1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1
        
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j-1]
        
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i-1][j]
        
        return [row[:n] for row in diff[:n]]
