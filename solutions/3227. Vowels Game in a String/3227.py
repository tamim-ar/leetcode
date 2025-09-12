class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        for c in s:
            if c in vowels:
                return True
        return False
