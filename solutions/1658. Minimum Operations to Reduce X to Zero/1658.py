class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # If the remaining subarray should have sum 0,
        # we need to remove all elements.
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        longest = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else len(nums) - longest
