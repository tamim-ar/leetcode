from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Max value of nums[i] is 10^5. Max target value `2 * nums[j]` is 2*10^5.
        # Frequency array must be large enough to hold counts for these values.
        freq_array_size = 2 * 100000 + 1
        
        left_counts = [0] * freq_array_size
        right_counts = [0] * freq_array_size
        
        # Initially, all numbers are in the "right" partition.
        for num in nums:
            right_counts[num] += 1
            
        total_triplets = 0
        
        # Iterate through each element, considering it as the middle element nums[j].
        for val_j in nums:
            # Move the current element from the right partition to the left.
            # First, remove it from right_counts for the current calculation.
            right_counts[val_j] -= 1
            
            target_val = 2 * val_j
            
            # Since max(nums[i])=10^5, target_val <= 200000, which is a valid index.
            count_i = left_counts[target_val]
            count_k = right_counts[target_val]
                
            term = count_i * count_k
            total_triplets = (total_triplets + term) % MOD
            
            # Now, add the current element to left_counts for subsequent iterations.
            left_counts[val_j] += 1
            
        return total_triplets