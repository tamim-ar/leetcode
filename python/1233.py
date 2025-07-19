from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)
        return res
