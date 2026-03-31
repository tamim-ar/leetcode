class Solution:
    def generateString(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)
        ans = ["$"] * (n + m - 1)
        for i in range(n):
            if s1[i] == "T":
                for j in range(m):
                    if ans[i + j] != "$" and ans[i + j] != s2[j]:
                        return ""
                    ans[i + j] = s2[j]

        b = [False] * (n + m - 1)
        for i in range(len(ans)):
            if ans[i] == "$":
                ans[i] = "a"
                b[i] = True

        for i in range(n):
            if s1[i] == "F":
                flag = True
                for j in range(m):
                    if ans[i + j] != s2[j]:
                        flag = False
                        break
                if flag:
                    flag2 = True
                    for j in range(m - 1, -1, -1):
                        if b[i + j]:
                            ans[i + j] = "b"
                            flag2 = False
                            break
                    if flag2:
                        return ""

        return "".join(ans)