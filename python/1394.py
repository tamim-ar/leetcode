from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        count = Counter(arr)
        res = [num for num, freq in count.items() if num == freq]
        return max(res) if res else -1
