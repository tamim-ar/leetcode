from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Example usage:
# recentCounter = RecentCounter()
# print(recentCounter.ping(1))    # 1
# print(recentCounter.ping(100))  # 2
# print(recentCounter.ping(3001)) # 3
# print(recentCounter.ping(3002)) # 3
