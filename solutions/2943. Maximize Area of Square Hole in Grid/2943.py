class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        max_h = cur = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            max_h = max(max_h, cur)
        
        max_v = cur = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            max_v = max(max_v, cur)
        
        side = min(max_h + 1, max_v + 1)
        return side * side
