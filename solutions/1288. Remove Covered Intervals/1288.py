class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, and end descending if starts are equal
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remaining = 0
        max_end = -1

        for start, end in intervals:
            if end > max_end:
                remaining += 1
                max_end = end

        return remaining