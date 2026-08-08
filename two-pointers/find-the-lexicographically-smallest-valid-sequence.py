class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = number of characters of word2
        # that can be matched from word1[i:] exactly.
        suf = [0] * (n + 1)
        suf[n] = m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = j + 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            # Normal exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not changed and suf[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                changed = True

            if j == m:
                return ans

        return []