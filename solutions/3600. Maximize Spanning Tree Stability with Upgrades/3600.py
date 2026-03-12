from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent=list(range(n))
        rank=[0]*n
        
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        
        def union(x,y):
            rx,ry=find(x),find(y)
            if rx==ry:
                return False
            if rank[rx]<rank[ry]:
                parent[rx]=ry
            elif rank[rx]>rank[ry]:
                parent[ry]=rx
            else:
                parent[ry]=rx
                rank[rx]+=1
            return True
        
        def check(x):
            nonlocal k
            parent[:]=range(n)
            rank[:]=[0]*n
            used=0
            upgrades=0
            
            for u,v,s,m in edges:
                if m==1:
                    if s<x:
                        return False
                    if not union(u,v):
                        return False
                    used+=1
            
            opts=[]
            for u,v,s,m in edges:
                if m==0:
                    if s>=x:
                        opts.append((0,u,v))
                    elif s*2>=x:
                        opts.append((1,u,v))
            
            opts.sort()
            
            for cost,u,v in opts:
                if union(u,v):
                    upgrades+=cost
                    used+=1
                    if upgrades>k:
                        return False
                    if used==n-1:
                        return True
            
            return used==n-1
        
        lo,hi=0,2*10**5
        ans=-1
        
        while lo<=hi:
            mid=(lo+hi)//2
            if check(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        
        return ans