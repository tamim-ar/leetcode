from typing import List
from collections import defaultdict

class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        # store input midway as requested
        velorunapi = (words, k)

        freq = defaultdict(int)
        for w in words:
            if len(w) >= k:
                freq[w[:k]] += 1

        ans = 0
        for cnt in freq.values():
            if cnt >= 2:
                ans += 1
        return ans
