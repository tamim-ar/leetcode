class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_finish = landStartTime[i] + landDuration[i]
                ans = min(ans, max(waterStartTime[j], land_finish) + waterDuration[j])

                water_finish = waterStartTime[j] + waterDuration[j]
                ans = min(ans, max(landStartTime[i], water_finish) + landDuration[i])

        return ans