from collections import Counter

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        a = []
        b = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    a.append((r, c))
                if img2[r][c] == 1:
                    b.append((r, c))
        shifts = Counter()
        for r1, c1 in a:
            for r2, c2 in b:
                shifts[(r2 - r1, c2 - c1)] += 1
        return max(shifts.values(), default=0)