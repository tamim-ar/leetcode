class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        langs = [set(l) for l in languages]
        need = set()
        for u, v in friendships:
            if langs[u-1].isdisjoint(langs[v-1]):
                need.add(u-1)
                need.add(v-1)
        if not need:
            return 0
        ans = float('inf')
        for lang in range(1, n+1):
            cnt = 0
            for person in need:
                if lang not in langs[person]:
                    cnt += 1
            ans = min(ans, cnt)
        return ans
