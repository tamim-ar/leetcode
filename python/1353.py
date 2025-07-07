import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()
        heap = []
        res, day, i, n = 0, 0, 0, len(events)

        while heap or i < n:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1
                day += 1

        return res
