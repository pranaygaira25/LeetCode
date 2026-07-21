class Solution(object):
    def minimumDistance(self, word):
        memo = {}
        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)
        def dist(a, b):
            if a is None:
                return 0
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        def dp(i, f1, f2):
            key = (i, f1, f2)
            if key in memo:
                return memo[key]
            if i == len(word):
                return 0
            target = get_pos(word[i])
            cost1 = dist(f1, target) + dp(i + 1, target, f2)
            cost2 = dist(f2, target) + dp(i + 1, f1, target)

            memo[key] = min(cost1, cost2)
            return memo[key]

        return dp(0, None, None)