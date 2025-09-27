import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            val = heapq.heappop(self.heap)
            self.added.remove(val)
            return val
        self.curr += 1
        return self.curr - 1

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
