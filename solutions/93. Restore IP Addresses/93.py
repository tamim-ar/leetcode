class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        res = []

        def backtrack(i, parts, curr):
            if parts == 4:
                if i == len(s):
                    res.append(curr[:-1])
                return
            for j in range(i, min(i+3, len(s))):
                seg = s[i:j+1]
                if (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
                    break
                backtrack(j+1, parts+1, curr + seg + '.')

        backtrack(0, 0, "")
        return res
