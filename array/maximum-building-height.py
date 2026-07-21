class Solution(object):
    def maxBuilding(self, n, restrictions):
        if not restrictions:
            return n - 1

        restrictions.append([1, 0])
        restrictions.sort()

        m = len(restrictions)

        # Left to right
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
            )

        # Right to left
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0

        # Maximum height between adjacent restrictions
        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            dist = x2 - x1
            ans = max(ans, (h1 + h2 + dist) // 2)

        # Buildings after the last restriction
        last_pos, last_h = restrictions[-1]
        ans = max(ans, last_h + (n - last_pos))

        return ans