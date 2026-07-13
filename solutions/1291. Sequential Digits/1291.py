class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"

        for length in range(2, 10):
            for i in range(10 - length):
                num = int(digits[i:i + length])
                if low <= num <= high:
                    result.append(num)

        return result