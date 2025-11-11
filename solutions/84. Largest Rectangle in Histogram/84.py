from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n + 1):
            cur = heights[i] if i < n else 0
            while stack and cur < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                max_area = max(max_area, h * (i - left))
            stack.append(i)
        return max_area
