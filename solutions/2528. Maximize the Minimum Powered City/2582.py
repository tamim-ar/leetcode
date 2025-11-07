class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[i] = prefix[right + 1] - prefix[left]
        
        def can(mid):
            added = [0] * n
            total_add = 0
            cur_sum = 0
            for i in range(n):
                if i - r - 1 >= 0:
                    cur_sum -= added[i - r - 1]
                if power[i] + cur_sum < mid:
                    need = mid - (power[i] + cur_sum)
                    if need > k - total_add:
                        return False
                    added_pos = min(n - 1, i + r)
                    added[added_pos] += need
                    cur_sum += need
                    total_add += need
                if i + r < n:
                    cur_sum += 0
            return True
        
        low, high = 0, sum(stations) + k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
