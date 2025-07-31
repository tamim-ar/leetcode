class Solution:
    def subarrayBitwiseORs(self, arr):
        s = []
        l = 0

        for a in arr:
            r = len(s)
            s.append(a)
            for i in range(l, r):
                if s[-1] != (s[i] | a):
                    s.append(s[i] | a)
            l = r

        return len(set(s))
