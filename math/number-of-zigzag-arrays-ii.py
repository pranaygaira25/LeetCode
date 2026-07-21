class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        sz = 2 * m

        def mat_mul(A, B):
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                Ai = A[i]
                Ci = C[i]
                for k in range(sz):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(sz):
                        Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_pow(M, e):
            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while e:
                if e & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                e >>= 1
            return R

        T = [[0] * sz for _ in range(sz)]

        for x in range(m):
            for y in range(x + 1, m):
                T[m + x][y] = 1

            for y in range(x):
                T[x][m + y] = 1

        P = mat_pow(T, n - 1)

        ans = 0
        for i in range(sz):
            for j in range(sz):
                ans = (ans + P[i][j]) % MOD

        return ans