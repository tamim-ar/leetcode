class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(x: str) -> str:
            parts = []
            bal = 0
            start = 0
            for i, ch in enumerate(x):
                bal += 1 if ch == '1' else -1
                if bal == 0:
                    inner = solve(x[start + 1:i])
                    parts.append("1" + inner + "0")
                    start = i + 1
            parts.sort(reverse=True)
            return "".join(parts)
        
        return solve(s)