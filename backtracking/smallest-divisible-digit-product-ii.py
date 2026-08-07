class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Prime factor counts for each digit
        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
            0: (0, 0, 0, 0),
        }

        # Factorize t
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]
        x = t
        for i, p in enumerate(primes):
            while x % p == 0:
                need[i] += 1
                x //= p
        if x != 1:
            return "-1"

        n = len(num)

        # Prefix factor counts
        prefix = [[0, 0, 0, 0] for _ in range(n + 1)]
        zero_found = False
        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                zero_found = True
            a, b, c, d7 = digit_factors[d]
            prefix[i + 1][0] = prefix[i][0] + a
            prefix[i + 1][1] = prefix[i][1] + b
            prefix[i + 1][2] = prefix[i][2] + c
            prefix[i + 1][3] = prefix[i][3] + d7

        # Already valid
        if not zero_found:
            ok = True
            for i in range(4):
                if prefix[n][i] < need[i]:
                    ok = False
            if ok:
                return num

        # Build minimal digit multiset
        def build_digits(req):
            a, b, c, d = req
            res = []

            while a >= 3:
                res.append('8')
                a -= 3
            if a == 2:
                res.append('4')
            elif a == 1:
                res.append('2')

            while b >= 2:
                res.append('9')
                b -= 2
            if b == 1:
                res.append('3')

            res += ['5'] * c
            res += ['7'] * d
            res.sort()
            return res

        # Feasibility
        def feasible(req, slots):
            return len(build_digits(req)) <= slots

        # Try changing from right to left
        for i in range(n - 1, -1, -1):
            cur = int(num[i])

            pref = prefix[i][:]

            if cur != 0:
                f = digit_factors[cur]
                for k in range(4):
                    pref[k] -= f[k]

            start = max(cur + 1, 1)

            for nd in range(start, 10):
                if nd == 0:
                    continue

                req = [
                    max(0, need[k] - pref[k] - digit_factors[nd][k])
                    for k in range(4)
                ]

                slots = n - i - 1

                if feasible(req, slots):
                    digits = build_digits(req)
                    ones = ['1'] * (slots - len(digits))
                    suffix = "".join(ones + digits)
                    return num[:i] + str(nd) + suffix

        # Need longer length
        length = n + 1
        digits = build_digits(need)
        ones = ['1'] * (length - len(digits))
        return "".join(ones + digits)