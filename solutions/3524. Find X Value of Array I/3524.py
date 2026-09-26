class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            r = num % k

            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[r] += 1

            # Extend every previous subarray
            for rem in range(k):
                new_dp[(rem * r) % k] += dp[rem]

            dp = new_dp

            # Add all subarrays ending at current position
            for rem in range(k):
                ans[rem] += dp[rem]

        return ans