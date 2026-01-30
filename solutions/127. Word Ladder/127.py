from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nw = word[:i] + c + word[i+1:]
                    if nw in wordSet:
                        wordSet.remove(nw)
                        q.append((nw, level + 1))
        return 0
