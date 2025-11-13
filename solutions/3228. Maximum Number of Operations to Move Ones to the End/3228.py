class Solution:
    def maxOperations(self, s: str) -> int:
        one = ans = 0
        for c in s:
            if c=='1': one+=1
            else: ans+=one
        return ans
