class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            value = ord('z') - ord(ch) + 1
            ans += value * (i + 1)

        return ans