class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = count = 0
        for n in nums:
            if n == 0:
                count += 1
                ans += count
            else:
                count = 0
        return ans
