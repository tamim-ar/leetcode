from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            prev1 = prev2 = 0
            for num in arr:
                prev1, prev2 = max(prev2 + num, prev1), prev1
            return prev1

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))