import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        occupied = []
        count = [0] * n

        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(occupied, (end, room))
            else:
                earliest_end, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (earliest_end + end - start, room))
            count[room] += 1

        return count.index(max(count))
