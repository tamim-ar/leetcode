class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum value is odd, all evens can subtract it to become odd
        if min_val % 2 == 1:
            return True
        
        # If the minimum value is even, we can only succeed if all numbers are already even
        return all(x % 2 == 0 for x in nums1)