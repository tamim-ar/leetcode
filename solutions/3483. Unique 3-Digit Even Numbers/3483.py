from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        counts = Counter(digits)
        valid_count = 0
        
        # Check every 3-digit even number from 100 to 998
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            req = Counter([d1, d2, d3])
            
            if all(counts[d] >= req[d] for d in req):
                valid_count += 1
                
        return valid_count