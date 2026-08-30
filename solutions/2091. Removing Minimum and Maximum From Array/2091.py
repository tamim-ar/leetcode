class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        front = right + 1
        back = n - left
        both_sides = (left + 1) + (n - right)

        return min(front, back, both_sides)