from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap, total, res = [], 0, 0
        for num2, num1 in pairs:
            heapq.heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)
        return res
