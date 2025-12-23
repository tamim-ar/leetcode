class Solution:
    def maxTwoEvents(self, events):
        events.sort()
        import heapq
        h = []
        best = 0
        ans = 0
        for s, e, v in events:
            while h and h[0][0] < s:
                best = max(best, heapq.heappop(h)[1])
            ans = max(ans, best + v, v)
            heapq.heappush(h, (e, v))
        return ans
