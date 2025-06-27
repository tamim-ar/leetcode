from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_valid(sub):
            i = j = cnt = 0
            while j < len(s):
                if s[j] == sub[i]:
                    i += 1
                    if i == len(sub):
                        cnt += 1
                        if cnt == k:
                            return True
                        i = 0
                j += 1
            return False

        counter = Counter(s)
        chars = [c for c in counter if counter[c] >= k]
        chars.sort(reverse=True)

        queue = deque([""])
        res = ""
        while queue:
            cur = queue.popleft()
            for ch in chars:
                new_str = cur + ch
                if is_valid(new_str):
                    queue.append(new_str)
                    if len(new_str) > len(res) or (len(new_str) == len(res) and new_str > res):
                        res = new_str
        return res
