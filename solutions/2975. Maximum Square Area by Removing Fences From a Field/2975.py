from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        h_diff = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_diff.add(h[j] - h[i])
        
        max_side = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_diff:
                    max_side = max(max_side, d)
        
        if max_side == 0:
            return -1
        
        return (max_side * max_side) % MOD
