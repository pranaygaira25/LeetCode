class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        # Non-zero digits
        nz = []
        pref_cnt = [0] * (n + 1)

        for i, ch in enumerate(s):
            pref_cnt[i + 1] = pref_cnt[i]
            if ch != '0':
                nz.append(int(ch))
                pref_cnt[i + 1] += 1

        m = len(nz)

        # Powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix concatenated value and prefix digit sum
        pref_val = [0] * (m + 1)
        pref_sum = [0] * (m + 1)

        for i in range(m):
            pref_val[i + 1] = (pref_val[i] * 10 + nz[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + nz[i]

        ans = []

        for l, r in queries:
            a = pref_cnt[l]
            b = pref_cnt[r + 1] - 1

            if a > b:
                ans.append(0)
                continue

            length = b - a + 1

            x = (pref_val[b + 1] - pref_val[a] * pow10[length]) % MOD
            digit_sum = pref_sum[b + 1] - pref_sum[a]

            ans.append((x * digit_sum) % MOD)

        return ans