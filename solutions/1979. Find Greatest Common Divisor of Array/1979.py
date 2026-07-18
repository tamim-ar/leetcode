class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = min(nums)
        b = max(nums)

        while b:
            a, b = b, a % b

        return a