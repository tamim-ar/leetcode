class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        prefix = 0
        # min_prefix[r] := minimum prefix sum seen so far at indices i where i % k == r
        min_prefix = [float("inf")] * k
        # before any elements, "index" is -1 → (-1) % k = k-1, so initialize that class
        min_prefix[(k - 1) % k] = 0  
        ans = -10**30  # or float("-inf")

        for i, x in enumerate(nums):
            prefix += x
            r = i % k
            # subarray ending at i with length divisible by k → same remainder class
            ans = max(ans, prefix - min_prefix[r])
            # update the min prefix sum for this remainder class
            if prefix < min_prefix[r]:
                min_prefix[r] = prefix

        return ans
