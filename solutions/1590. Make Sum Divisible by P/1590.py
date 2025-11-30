class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0
        mp = {0: -1}
        cur = 0
        res = len(nums)
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            need = (cur - total) % p
            if need in mp:
                res = min(res, i - mp[need])
            mp[cur] = i
        return res if res < len(nums) else -1
