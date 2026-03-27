class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        
        for i in range(m):
            row = mat[i]
            if i % 2 == 0:
                if row != row[k:] + row[:k]:
                    return False
            else:
                if row != row[-k:] + row[:-k]:
                    return False
        
        return True