
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                ans += len(distinct) ** 2

        return ans
