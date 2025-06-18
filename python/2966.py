class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if group[-1] - group[0] > k:
                return []
            res.append(group)
        return res
