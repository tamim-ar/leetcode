class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1

        ans += min(prev, curr)
        return ans
