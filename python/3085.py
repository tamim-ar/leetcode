import collections
import math  # optional

class Solution:
    def minimumDeletions(self, word, k):
        freq = collections.Counter(word)
        ans = float('inf')  # use float('inf') for compatibility

        for minFreq in freq.values():
            deletions = 0
            for count in freq.values():
                if count < minFreq:
                    deletions += count
                elif count > minFreq + k:
                    deletions += count - (minFreq + k)
            ans = min(ans, deletions)

        return ans
