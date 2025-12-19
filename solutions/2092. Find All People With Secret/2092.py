class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])
        know = {0, firstPerson}
        i = 0
        m = len(meetings)
        while i < m:
            t = meetings[i][2]
            parent = {}
            def find(x):
                parent.setdefault(x, x)
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            def union(a, b):
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[rb] = ra
            j = i
            people = set()
            while j < m and meetings[j][2] == t:
                x, y, _ = meetings[j]
                union(x, y)
                people.add(x)
                people.add(y)
                j += 1
            comp = {}
            for p in people:
                r = find(p)
                comp.setdefault(r, []).append(p)
            for group in comp.values():
                if any(p in know for p in group):
                    know.update(group)
            i = j
        return list(know)
