class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        from functools import cache
      
        MOD = 10**9 + 7
      
        @cache
        def count_arrays(zeros_left: int, ones_left: int, last_digit: int) -> int:
            """
            Count valid stable arrays with given zeros and ones remaining.
          
            Args:
                zeros_left: Number of zeros still to place
                ones_left: Number of ones still to place  
                last_digit: The last digit placed (0 or 1)
          
            Returns:
                Number of valid stable arrays
            """
            # Base case: only ones left
            if zeros_left == 0:
                # Valid if last digit was 1 and remaining ones don't exceed limit
                return int(last_digit == 1 and ones_left <= limit)
          
            # Base case: only zeros left
            if ones_left == 0:
                # Valid if last digit was 0 and remaining zeros don't exceed limit
                return int(last_digit == 0 and zeros_left <= limit)
          
            # If last digit was 0, we're placing another 0
            if last_digit == 0:
                # Add one more 0 to the sequence
                total = count_arrays(zeros_left - 1, ones_left, 0) + count_arrays(zeros_left - 1, ones_left, 1)
              
                # Subtract invalid cases where we exceed limit consecutive zeros
                # This happens when we have more than 'limit' consecutive zeros
                if zeros_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left - limit - 1, ones_left, 1)
              
                return total
          
            # If last digit was 1, we're placing another 1
            else:
                # Add one more 1 to the sequence
                total = count_arrays(zeros_left, ones_left - 1, 0) + count_arrays(zeros_left, ones_left - 1, 1)
              
                # Subtract invalid cases where we exceed limit consecutive ones
                # This happens when we have more than 'limit' consecutive ones
                if ones_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left, ones_left - limit - 1, 0)
              
                return total
      
        # Calculate total by considering both starting with 0 and starting with 1
        result = (count_arrays(zero, one, 0) + count_arrays(zero, one, 1)) % MOD
      
        # Clear the cache to free memory
        count_arrays.cache_clear()
      
        return result
