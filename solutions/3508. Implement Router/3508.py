from collections import deque, defaultdict
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.q) == self.memoryLimit:
            old_src, old_dst, old_time = self.q.popleft()
            self.seen.remove((old_src, old_dst, old_time))
            self.dest_map[old_dst].pop(0)
        self.q.append(key)
        self.seen.add(key)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        src, dst, ts = self.q.popleft()
        self.seen.remove((src, dst, ts))
        self.dest_map[dst].pop(0)
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.dest_map[destination]
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] < startTime:
                l = m + 1
            else:
                r = m
        left = l
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] <= endTime:
                l = m + 1
            else:
                r = m
        right = l
        return right - left
