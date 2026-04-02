class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            # detected loop
            if i in visit: 
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                # detected loop
                if not dfs(j, i):
                    return False
            return True # did not detect loop

        # ensure graph is a tree by checking all nodes are connected
        return dfs(0, -1) and n == len(visit)