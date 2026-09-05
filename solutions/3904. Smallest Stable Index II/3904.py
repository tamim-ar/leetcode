class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] = minimum value in nums[i..n-1]
        suffix_min = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # prefix_max tracks the maximum value in nums[0..i] as we iterate
        prefix_max = 0
        for i, x in enumerate(nums):
            prefix_max = max(prefix_max, x)
            # Check whether the gap between the prefix max and suffix min
            # at index i is within the allowed threshold k
            if prefix_max - suffix_min[i] <= k:
                return i

        # No index satisfies the condition
        return -1
