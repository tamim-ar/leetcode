class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for w in words[1:]:
            if sorted(w) != sorted(res[-1]):
                res.append(w)
        return res
