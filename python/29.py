class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return -result if negative else result
