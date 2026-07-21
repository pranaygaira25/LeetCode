class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        arr = []
        for row in grid:
            arr.extend(row)

        arr = arr[-k:] + arr[:-k]

        res = []
        idx = 0
        for i in range(m):
            res.append(arr[idx:idx + n])
            idx += n

        return res