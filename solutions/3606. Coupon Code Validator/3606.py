class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_business = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        res = []
        for c, b, a in zip(code, businessLine, isActive):
            if a and c and all(ch.isalnum() or ch == '_' for ch in c) and b in valid_business:
                res.append((valid_business[b], c))
        res.sort()
        return [c for _, c in res]
