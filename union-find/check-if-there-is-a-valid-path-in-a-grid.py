from collections import deque

class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # directions: (dx, dy)
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        # check if two cells connect properly
        def is_connected(x1, y1, x2, y2):
            dx, dy = x2 - x1, y2 - y1
            return (-dx, -dy) in dirs[grid[x2][y2]]
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if is_connected(x, y, nx, ny):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False