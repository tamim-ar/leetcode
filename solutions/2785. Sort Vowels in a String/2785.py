class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [c for c in s if c in 'aeiouAEIOU']
        vowels.sort()
        it = iter(vowels)
        res = []
        for c in s:
            if c in 'aeiouAEIOU':
                res.append(next(it))
            else:
                res.append(c)
        return ''.join(res)
