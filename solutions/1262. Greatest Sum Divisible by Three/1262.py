class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for x in nums:
            r = x % 3
            ndp = dp[:]
            for i in range(3):
                ndp[(i + r) % 3] = max(ndp[(i + r) % 3], dp[i] + x)
            dp = ndp
        return dp[0]
