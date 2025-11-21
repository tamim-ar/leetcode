class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            l = s.find(c)
            r = s.rfind(c)
            if l < r:
                res += len(set(s[l+1:r]))
        return res
