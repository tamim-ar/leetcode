from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1) // 2
        set1, set2 = set(nums1), set(nums2)
        
        # Count unique elements in each array
        only1 = set1 - set2
        only2 = set2 - set1
        common = set1 & set2
        
        # Take min(n, len(only_x)) elements from each array's unique elements
        take1 = min(n, len(only1))
        take2 = min(n, len(only2))
        
        # If we haven't used our quota, take from common elements
        remaining1 = min(n - take1, len(common))
        remaining2 = min(n - take2, len(common) - remaining1)
        
        return take1 + take2 + remaining1 + remaining2