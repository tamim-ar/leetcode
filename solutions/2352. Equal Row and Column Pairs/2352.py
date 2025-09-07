from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(r) for r in grid)
        cols = [tuple(grid[r][c] for r in range(len(grid))) for c in range(len(grid))]
        return sum(rows[col] for col in cols)
