class Solution(object):
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]
        
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        ans = float("inf")
        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        
        while stack:
            u = stack.pop()
            for v, d in graph[u]:
                ans = min(ans, d)
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        
        return ans