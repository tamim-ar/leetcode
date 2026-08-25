class Solution:
    def singleNumber(self, nums):
        xor_all = 0

        # XOR all numbers
        for num in nums:
            xor_all ^= num

        # Get the rightmost set bit
        diff = xor_all & -xor_all

        a = 0
        b = 0

        # Divide numbers into two groups
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]