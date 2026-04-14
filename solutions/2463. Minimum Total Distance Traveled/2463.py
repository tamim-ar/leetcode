class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        slots = []
        for pos, limit in factory:
            slots += [pos] * limit
        
        n, m = len(robot), len(slots)
        INF = float('inf')
        
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j - 1]
                dp[i][j] = min(dp[i][j],
                               dp[i - 1][j - 1] + abs(robot[i - 1] - slots[j - 1]))
        
        return dp[n][m]