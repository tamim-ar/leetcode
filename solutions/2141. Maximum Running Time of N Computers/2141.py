from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        left, right = 0, total // n

        while left < right:
            mid = (left + right + 1) // 2
            if sum(min(b, mid) for b in batteries) >= mid * n:
                left = mid
            else:
                right = mid - 1

        return left
