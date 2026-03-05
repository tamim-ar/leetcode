class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0
        c2 = 0
        
        for i, ch in enumerate(s):
            if ch != ('0' if i % 2 == 0 else '1'):
                c1 += 1
            if ch != ('1' if i % 2 == 0 else '0'):
                c2 += 1
        
        return min(c1, c2)