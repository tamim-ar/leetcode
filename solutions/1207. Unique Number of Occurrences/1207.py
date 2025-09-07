from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return len(set(freq.values())) == len(freq.values())
