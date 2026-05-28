class TrieNode:
    def __init__(self):
        self.children = {}
        self.best = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best_idx]):
                best_idx = i

        def better(i, j):
            if j == -1:
                return i
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i
            if len(wordsContainer[i]) == len(wordsContainer[j]) and i < j:
                return i
            return j

        root.best = best_idx

        for i, word in enumerate(wordsContainer):
            node = root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                node.best = better(i, node.best)

        ans = []

        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best)

        return ans