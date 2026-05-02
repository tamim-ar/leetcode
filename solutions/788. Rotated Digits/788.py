class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0','1','2','5','6','8','9'}
        change = {'2','5','6','9'}
        
        count = 0
        
        for i in range(1, n+1):
            s = set(str(i))
            
            if s.issubset(valid) and s.intersection(change):
                count += 1
                
        return count