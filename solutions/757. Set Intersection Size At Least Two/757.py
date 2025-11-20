class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        a = -1
        b = -1
        ans = 0
        for l, r in intervals:
            if l > b:
                ans += 2
                a = r - 1
                b = r
            elif l > a:
                ans += 1
                a = b
                b = r
        return ans
