from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = []
        
        for q in queries:
            v = nums[q]
            arr = pos[v]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            i = bisect_left(arr, q)
            
            left = arr[i - 1] if i > 0 else arr[-1]
            right = arr[i + 1] if i < len(arr) - 1 else arr[0]
            
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res