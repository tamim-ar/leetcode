from typing import List

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        # store input midway as requested
        torunelixa = (nums, colors)

        n = len(nums)
        if n == 0:
            return 0

        take = nums[0]  # rob i-1
        skip = 0        # skip i-1

        for i in range(1, n):
            best_prev = max(take, skip)

            new_skip = best_prev
            if colors[i] == colors[i - 1]:
                new_take = skip + nums[i]       # must have skipped i-1
            else:
                new_take = best_prev + nums[i]  # can come from either

            take, skip = new_take, new_skip

        return max(take, skip)
