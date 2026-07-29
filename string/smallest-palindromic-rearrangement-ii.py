from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        half = {}
        m = 0

        for ch in sorted(cnt):
            if cnt[ch] & 1:
                mid = ch
            half[ch] = cnt[ch] // 2
            m += half[ch]

        LIMIT = k

        def count_perm(freq, total):
            res = 1
            rem = total
            for ch in sorted(freq):
                c = freq[ch]
                if c:
                    res *= comb(rem, c)
                    if res > LIMIT:
                        return LIMIT + 1
                    rem -= c
            return res

        if count_perm(half, m) < k:
            return ""

        left = []

        while m:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half, m - 1)

                if ways >= k:
                    left.append(ch)
                    m -= 1
                    break
                else:
                    k -= ways
                    half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]