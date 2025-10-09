class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        dp = [0] * n
        for j in range(m):
            new_dp = [0] * n
            new_dp[0] = dp[0] + skill[0] * mana[j]
            for i in range(1, n):
                new_dp[i] = skill[i] * mana[j] + max(dp[i], new_dp[i - 1])
            dp = new_dp
        return dp[-1]
