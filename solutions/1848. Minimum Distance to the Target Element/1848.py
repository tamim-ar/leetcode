class Solution:
    def getMinDistance(self, nums, target, start):
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
        return ans