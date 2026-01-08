class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[-10**18] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                dp[i+1][j+1] = max(
                    prod,
                    dp[i][j] + prod,
                    dp[i][j+1],
                    dp[i+1][j]
                )
        return dp[n][m]
