class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        res = []
        
        for c in range(cols):
            i, j = 0, c
            while i < rows and j < cols:
                res.append(encodedText[i * cols + j])
                i += 1
                j += 1
        
        return ''.join(res).rstrip()