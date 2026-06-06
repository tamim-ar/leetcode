class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            total -= num
            ans.append(abs(left - total))
            left += num

        return ans