class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count, end = 0, float('-inf')
        for s, e in intervals:
            if s < end:
                count += 1
            else:
                end = e
        return count
