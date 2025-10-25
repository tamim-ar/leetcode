class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        day = 1
        
        for i in range(1, n + 1):
            total += week + day
            day += 1
            if day > 7:
                week += 1
                day = 1
        
        return total
