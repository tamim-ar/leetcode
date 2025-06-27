from itertools import combinations_with_replacement

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter

        counter = Counter(s)
        chars = [ch for ch in counter if counter[ch] >= k]
        chars.sort(reverse=True)

        def is_valid(sub):
            i = 0
            cnt = 0
            for ch in s:
                if ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        cnt += 1
                        i = 0
                        if cnt == k:
                            return True
            return False

        max_len = len(s) // k
        res = ""
        for l in range(1, max_len + 1):
            for comb in combinations_with_replacement(chars, l):
                for perm in set(permutations(comb)):
                    sub = ''.join(perm)
                    if is_valid(sub) and (len(sub) > len(res) or (len(sub) == len(res) and sub > res)):
                        res = sub
        return res
