class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        q_diff = left_q - right_q
        sum_diff = left_sum - right_sum

        if q_diff == 0:
            return sum_diff != 0

        if abs(q_diff) % 2 == 1:
            return True

        return abs(sum_diff) != 9 * abs(q_diff) // 2