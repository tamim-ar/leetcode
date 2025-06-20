class Solution:
    def maxDistance(self, s, k):
        ans = 0
        # Try all 4 direction combos
        for d1, d2 in [('N','E'), ('N','W'), ('S','E'), ('S','W')]:
            pos = 0
            rem = k
            for ch in s:
                if ch == d1 or ch == d2:
                    pos += 1
                elif rem > 0:
                    rem -= 1
                    pos += 1
                else:
                    pos -= 1
                ans = max(ans, pos)
        return ans
