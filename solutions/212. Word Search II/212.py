from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m, n = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None  # Avoid duplicates

            board[r][c] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = ch

            # Prune Trie
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return ans