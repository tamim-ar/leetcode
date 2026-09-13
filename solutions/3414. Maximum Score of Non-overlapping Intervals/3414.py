from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store original indices and sort by left boundary
        sorted_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            sorted_intervals.append((l, r, w, i))
        sorted_intervals.sort()
        
        # Extract left endpoints for binary search
        left_bounds = [interval[0] for interval in sorted_intervals]
        
        # dp[i][k] stores (max_weight, list_of_original_indices)
        # using up to k intervals from suffix sorted_intervals[i:]
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, weight, original_idx = sorted_intervals[i]
            
            # Find the next non-overlapping interval (first with left boundary > r)
            nxt = bisect_right(left_bounds, r)
            
            for k in range(1, 5):
                # Choice 1: Skip current interval
                best_weight, best_indices = dp[i + 1][k]
                
                # Choice 2: Pick current interval
                next_weight, next_indices = dp[nxt][k - 1]
                cand_weight = weight + next_weight
                cand_indices = sorted([original_idx] + next_indices)
                
                # Update dp state with the best choice
                if cand_weight > best_weight:
                    dp[i][k] = (cand_weight, cand_indices)
                elif cand_weight == best_weight:
                    if not best_indices or cand_indices < best_indices:
                        dp[i][k] = (cand_weight, cand_indices)
                    else:
                        dp[i][k] = (best_weight, best_indices)
                else:
                    dp[i][k] = (best_weight, best_indices)
                    
        return dp[0][4][1]