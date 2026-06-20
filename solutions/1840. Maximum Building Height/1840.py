from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # add building 1 and building n
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # sort by building index
        restrictions.sort()
        
        # left to right pass
        for i in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[i - 1]
            cur_id, cur_h = restrictions[i]
            restrictions[i][1] = min(cur_h, prev_h + (cur_id - prev_id))
        
        # right to left pass
        for i in range(len(restrictions) - 2, -1, -1):
            next_id, next_h = restrictions[i + 1]
            cur_id, cur_h = restrictions[i]
            restrictions[i][1] = min(cur_h, next_h + (next_id - cur_id))
        
        # find maximum possible peak between every two restrictions
        ans = 0
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]
            
            dist = x2 - x1
            peak = (h1 + h2 + dist) // 2
            ans = max(ans, peak)
        
        return ans