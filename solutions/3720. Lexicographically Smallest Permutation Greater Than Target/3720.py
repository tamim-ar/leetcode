from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        candidates = []
        
        # Keep track of characters we are forced to use to match the target's prefix
        running_counts = Counter()
        
        for i in range(n):
            # Check if we can perfectly match target[0...i-1]
            if i > 0:
                running_counts[target[i-1]] += 1
                # If target requires more of a character than `s` has, this prefix is invalid
                if running_counts[target[i-1]] > s_counts[target[i-1]]:
                    break 
                    
            # Calculate remaining available characters
            available = s_counts - running_counts
            
            # Find the smallest available character strictly greater than target[i]
            best_c = None
            for c in sorted(available.keys()):
                if c > target[i] and available[c] > 0:
                    best_c = c
                    break
            
            # If we found a valid character to exceed the target at index i
            if best_c:
                # 1. Start with the matching prefix + the exceeding character
                cand_prefix = target[:i] + best_c
                
                # 2. Update remaining counts after using best_c
                rem_counts = available.copy()
                rem_counts[best_c] -= 1
                
                # 3. Sort the rest of the available characters to make the suffix as small as possible
                cand_suffix = []
                for char in sorted(rem_counts.keys()):
                    cand_suffix.append(char * rem_counts[char])
                    
                # Store the fully formed candidate string
                candidates.append(cand_prefix + "".join(cand_suffix))
                
        if not candidates:
            return ""
            
        # Return the lexicographically smallest valid candidate
        return min(candidates)