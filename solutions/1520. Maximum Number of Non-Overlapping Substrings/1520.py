class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = [len(s)] * 26
        last = [-1] * 26

        # Find first and last occurrence of each character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so this interval cannot be valid.
                if first[idx] < l:
                    valid = False
                    break

                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        # Greedily choose the interval ending earliest
        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans