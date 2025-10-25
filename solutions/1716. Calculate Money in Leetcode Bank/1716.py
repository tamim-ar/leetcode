class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0
        
        # Sum of full weeks
        total += weeks * (28 + 7 * (weeks - 1) // 2 * 7)
        
        # Sum of remaining days
        total += days * (weeks + (days + 1) // 2) if days else 0
        total += sum(weeks + i + 1 for i in range(days))
        
        return total
