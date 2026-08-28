class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Count frequency of each character
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        # Check if a valid palindrome can be formed
        odd_count = 0
        odd_char = ""
        for i in range(26):
            if counts[i] % 2 != 0:
                odd_count += 1
                odd_char = chr(ord('a') + i)
                
        if odd_count > 1:
            return ""
            
        # Counts available for the first half
        half_counts = [count // 2 for count in counts]
        
        def build_palindrome(first_half: str) -> str:
            """Constructs the full palindrome from the first half."""
            mid = odd_char if n % 2 != 0 else ""
            return first_half + mid + first_half[::-1]

        best_result = ""

        # Try to match a prefix of length i from target's first half
        for i in range(half_len, -1, -1):
            curr_counts = list(half_counts)
            prefix = []
            possible = True

            # Match prefix target[0...i-1]
            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if curr_counts[idx] > 0:
                    curr_counts[idx] -= 1
                    prefix.append(target[j])
                else:
                    possible = False
                    break

            if not possible:
                continue

            if i == half_len:
                # Exact half matched; check if full palindrome > target
                pal = build_palindrome("".join(prefix))
                if pal > target:
                    if not best_result or pal < best_result:
                        best_result = pal
            else:
                # Place a character > target[i] at position i
                target_char_idx = ord(target[i]) - ord('a')
                for c in range(target_char_idx + 1, 26):
                    if curr_counts[c] > 0:
                        temp_counts = list(curr_counts)
                        temp_counts[c] -= 1
                        
                        # Build the rest of the first half using smallest available characters
                        first_half = "".join(prefix) + chr(ord('a') + c)
                        for k in range(26):
                            first_half += chr(ord('a') + k) * temp_counts[k]
                            
                        pal = build_palindrome(first_half)
                        if pal > target:
                            if not best_result or pal < best_result:
                                best_result = pal
                        break  # Found the smallest valid char > target[i] for this prefix

        return best_result