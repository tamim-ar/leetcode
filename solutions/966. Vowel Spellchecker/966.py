from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        lower_map = {}
        vowel_map = {}

        def devowel(word):
            return ''.join('*' if ch in 'aeiou' else ch for ch in word)

        for word in wordlist:
            lower = word.lower()
            if lower not in lower_map:
                lower_map[lower] = word
            vword = devowel(lower)
            if vword not in vowel_map:
                vowel_map[vword] = word

        ans = []
        for query in queries:
            if query in word_set:
                ans.append(query)
            else:
                lower = query.lower()
                if lower in lower_map:
                    ans.append(lower_map[lower])
                else:
                    vword = devowel(lower)
                    if vword in vowel_map:
                        ans.append(vowel_map[vword])
                    else:
                        ans.append("")
        return ans
