from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        l = 0
        best = 1
        
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            best = max(best, r - l + 1)
        
        return n - best
