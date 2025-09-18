import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        for u, t, p in tasks:
            self.task_map[t] = (u, p)
            heapq.heappush(self.heap, (-p, -t, u, t))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            p, t, u, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map and self.task_map[taskId] == (u, -p):
                del self.task_map[taskId]
                return u
        return -1
