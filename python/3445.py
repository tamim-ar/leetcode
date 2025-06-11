class Solution(object):
    def maxDifference(self, s, k):
        from collections import Counter
        
        n = len(s)
        max_diff = -1

        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                if j - i + 1 >= k:
                    odd_chars = [c for c in freq if freq[c] % 2 == 1]
                    even_chars = [c for c in freq if freq[c] % 2 == 0]
                    for a in odd_chars:
                        for b in even_chars:
                            diff = freq[a] - freq[b]
                            max_diff = max(max_diff, diff)
        return max_diff
