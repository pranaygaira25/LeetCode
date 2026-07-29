from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = []
        mid = ""
        for ch in sorted(cnt):
            if cnt[ch] % 2:
                mid = ch
            half.extend([ch] * (cnt[ch] // 2))

        n = len(half)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        def ways(freq):
            total = sum(freq.values())
            res = fact[total]
            for v in freq.values():
                res //= fact[v]
            return res

        freq = Counter(half)
        left = []

        for _ in range(n):
            for ch in sorted(freq):
                if freq[ch] == 0:
                    continue
                freq[ch] -= 1
                w = ways(freq)
                if k > w:
                    k -= w
                    freq[ch] += 1
                else:
                    left.append(ch)
                    break

        left = "".join(left)
        return left + mid + left[::-1]