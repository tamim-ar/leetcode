class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = {}
        dry_days = []
        res = [-1] * len(rains)

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                res[i] = 1
            else:
                if lake in full:
                    import bisect
                    idx = bisect.bisect_right(dry_days, full[lake])
                    if idx == len(dry_days):
                        return []
                    res[dry_days[idx]] = lake
                    dry_days.pop(idx)
                full[lake] = i
        return res
