class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Determines if Alice wins the sum game.
        Alice and Bob take turns replacing '?' with digits (0-9).
        Bob wins if sum of first half equals sum of second half.
        Alice wins otherwise.
      
        Args:
            num: String containing digits and '?' characters
      
        Returns:
            True if Alice wins, False if Bob wins
        """
        # Get the length of the string
        string_length = len(num)
      
        # Split the string into two halves
        first_half = num[:string_length // 2]
        second_half = num[string_length // 2:]
      
        # Count question marks in each half
        question_marks_first_half = first_half.count("?")
        question_marks_second_half = second_half.count("?")
      
        # Calculate sum of known digits in each half
        sum_first_half = sum(int(digit) for digit in first_half if digit != "?")
        sum_second_half = sum(int(digit) for digit in second_half if digit != "?")
      
        # Alice wins if:
        # 1. Total question marks is odd (Alice gets last move)
        # 2. The difference in sums doesn't match the expected value
        #    (Bob needs exactly 9 * (difference in question marks) / 2 to balance)
        total_question_marks = question_marks_first_half + question_marks_second_half
        sum_difference = sum_first_half - sum_second_half
        question_mark_difference = question_marks_second_half - question_marks_first_half
      
        return (total_question_marks % 2 == 1 or 
                sum_difference != 9 * question_mark_difference // 2)
