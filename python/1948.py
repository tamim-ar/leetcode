from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.key = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Step 1: Build the Trie
        for path in paths:
            node = root
            for folder in path:
                node = node.children[folder]

        serial_map = defaultdict(list)

        # Step 2: Serialize each subtree and record them
        def serialize(node):
            if not node.children:
                return ""
            serial = []
            for folder in sorted(node.children):
                child_serial = serialize(node.children[folder])
                serial.append(f"{folder}({child_serial})")
            key = "".join(serial)
            node.key = key
            serial_map[key].append(node)
            return key

        serialize(root)

        # Step 3: Mark duplicates
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        res = []

        # Step 4: DFS and collect valid paths
        def dfs(node, path):
            for folder, child in node.children.items():
                if not child.is_deleted:
                    path.append(folder)
                    res.append(list(path))
                    dfs(child, path)
                    path.pop()

        dfs(root, [])
        return res
