class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        min_penalty = penalty
        ans = 0
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i + 1
        return ans
