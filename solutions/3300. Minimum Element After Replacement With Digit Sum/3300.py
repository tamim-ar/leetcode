class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            ans = min(ans, digit_sum)

        return ans