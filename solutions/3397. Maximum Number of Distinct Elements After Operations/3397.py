from collections import Counter

class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        duplicates = []
        
        # Collect all duplicates
        for num, freq in count.items():
            if freq > 1:
                duplicates.extend([num] * (freq - 1))
        
        # Sort duplicates to adjust smallest first
        duplicates.sort()
        
        distinct_count = len(count)
        
        for dup in duplicates:
            if k == 0:
                break
            # Try to move the duplicate outside current set
            step = 1
            while step <= k:
                if dup - step not in count:
                    count[dup - step] = 1
                    distinct_count += 1
                    k -= step
                    break
                elif dup + step not in count:
                    count[dup + step] = 1
                    distinct_count += 1
                    k -= step
                    break
                step += 1
        
        return distinct_count
