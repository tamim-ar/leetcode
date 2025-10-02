class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            res += 1
            empty += 1
        return res
