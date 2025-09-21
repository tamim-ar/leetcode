import bisect

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            need = (success + s - 1) // s
            idx = bisect.bisect_left(potions, need)
            res.append(m - idx)
        return res
