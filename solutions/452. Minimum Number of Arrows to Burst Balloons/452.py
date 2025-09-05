class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows, end = 0, float('-inf')
        for s, e in points:
            if s > end:
                arrows += 1
                end = e
        return arrows
