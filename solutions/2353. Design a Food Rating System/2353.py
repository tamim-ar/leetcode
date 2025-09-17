from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        c = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            r, f = heap[0]
            if -r == self.food_to_rating[f]:
                return f
            heapq.heappop(heap)
