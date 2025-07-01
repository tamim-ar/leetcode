from typing import List

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        result = []
        total = 1
        i = 0

        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1]:
                count += 1
                i += 1
            total += (count - 1)
            result.append(f"{count}{word[i]}")
            i += 1

        return total

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # Find column maximums
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        
        # Replace -1s with column maximums
        answer = [row[:] for row in matrix]
        for i in range(m):
            for j in range(n):
                if answer[i][j] == -1:
                    answer[i][j] = col_max[j]
        
        return answer


print(Solution().possibleStringCount("abbcccc"))
print(Solution().possibleStringCount("abcd"))
print(Solution().possibleStringCount("aaaa"))
print(Solution().possibleStringCount("eae"))