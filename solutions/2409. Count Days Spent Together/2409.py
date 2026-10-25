
class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def dayOfYear(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days[:month - 1]) + day

        start = max(dayOfYear(arriveAlice), dayOfYear(arriveBob))
        end = min(dayOfYear(leaveAlice), dayOfYear(leaveBob))

        return max(0, end - start + 1)
