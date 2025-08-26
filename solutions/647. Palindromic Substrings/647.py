class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), 0
        for center in range(2 * n - 1):
            l, r = center // 2, (center + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
