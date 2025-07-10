from typing import List

class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)  # Total number of meetings
        max_free_time = 0  # Variable to hold the maximum free time found
      
        # Calculate the maximum gaps from the left side
        left_gaps = [0] * n
        left_gaps[0] = startTime[0]  # Free time before the first meeting starts
        for i in range(1, n):
            left_gaps[i] = max(left_gaps[i - 1], startTime[i] - endTime[i - 1])
      
        # Calculate the maximum gaps from the right side
        right_gaps = [0] * n
        right_gaps[n - 1] = eventTime - endTime[-1]  # Free time after the last meeting ends
        for i in range(n - 2, -1, -1):
            right_gaps[i] = max(right_gaps[i + 1], startTime[i + 1] - endTime[i])
      
        # Compute the maximum free time by evaluating each meeting
        for i in range(n):
            # Calculate the gap before the current meeting
            left_gap = left_gaps[i] if i == 0 else startTime[i] - endTime[i - 1]
            # Calculate the gap after the current meeting
            right_gap = right_gaps[i] if i == n - 1 else startTime[i + 1] - endTime[i]
          
            # Calculate the total interval of free time
            interval = 0
            if (
                i != 0
                and left_gaps[i - 1] >= (endTime[i] - startTime[i])
                or i != n - 1
                and right_gaps[i + 1] >= (endTime[i] - startTime[i])
            ):
                interval = endTime[i] - startTime[i]
          
            # Update the maximum free time found
            max_free_time = max(max_free_time, left_gap + interval + right_gap)
      
        return max_free_time
