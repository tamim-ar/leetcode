class Solution:
    def findKDistantIndices(self, nums, key, k):
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(max(0, i - k), min(n, i + k + 1)):
                if nums[j] == key:
                    res.append(i)
                    break
        return res
