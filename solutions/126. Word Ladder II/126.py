from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()
            for w in level:
                wordSet.discard(w)
            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nw = word[:i] + c + word[i+1:]
                        if nw in wordSet:
                            if nw == endWord:
                                found = True
                            next_level.add(nw)
                            parents[nw].add(word)
            level = next_level

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])
        return res
