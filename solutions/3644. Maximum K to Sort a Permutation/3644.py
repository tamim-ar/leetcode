
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = 0

        for i, x in enumerate(nums):
            if i != x:
                ans |= x

        if ans == 0:
            return 0

        ans = -1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x

        return ans
