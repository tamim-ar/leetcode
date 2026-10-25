# TC: O(n) where n is the length of nums
# SC: O(1)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # n is the array length, and k is the current 0-based index of value 0
        n, k = len(nums), nums.index(0)
        # Checks that every value is one greater than the previous value modulo n
        # If true, rotate left k times or simulate rotating right k times using n - k left rotations and two reversals
        if all(nums[i] == (nums[i - 1] + 1) % n for i in range(1, n)): return min(k, n - k + 2)
        # Checks that every value is one less than the previous value modulo n
        # If true, add one reversal and choose the cheaper rotation count depending on whether rotation happens before or after reversal
        if all(nums[i] == (nums[i - 1] - 1) % n for i in range(1, n)): return 1 + min((k + 1) % n, n - 1 - k)
        # If nums is neither cyclically increasing nor cyclically decreasing
        # The allowed operations cannot sort it
        return -1