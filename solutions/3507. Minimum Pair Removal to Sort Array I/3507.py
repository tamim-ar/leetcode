class Solution:
    def minimumPairRemoval(self, nums):
        ops = 0
        while True:
            ok = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    ok = False
                    break
            if ok:
                return ops

            min_sum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            ops += 1
