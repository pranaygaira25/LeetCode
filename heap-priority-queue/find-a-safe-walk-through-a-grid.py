from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        
        start = health - grid[0][0]
        if start <= 0:
            return False
        
        q = deque([(0, 0)])
        dist[0][0] = start
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            x, y = q.popleft()
            h = dist[x][y]
            
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > dist[nx][ny] and nh > 0:
                        dist[nx][ny] = nh
                        q.append((nx, ny))
        
        return False