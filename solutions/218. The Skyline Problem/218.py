from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        # Create start and end events
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start event
            events.append((right, 0, 0))           # End event

        # Sort by x, then by height
        events.sort()

        res = []
        heap = [(0, float('inf'))]  # (-height, right)

        for x, negH, right in events:

            # Remove expired buildings
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add new building if it is a start event
            if negH != 0:
                heapq.heappush(heap, (negH, right))

            # Current maximum height
            currHeight = -heap[0][0]

            # Add key point if height changes
            if not res or res[-1][1] != currHeight:
                res.append([x, currHeight])

        return res