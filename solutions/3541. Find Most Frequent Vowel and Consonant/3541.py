class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        max_vowel = max((freq[ch] for ch in vowels if ch in freq), default=0)
        max_consonant = max((freq[ch] for ch in freq if ch not in vowels), default=0)
        return max_vowel + max_consonant
