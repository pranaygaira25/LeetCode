class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        prefix = []
        quinorath = (s, target)
        i = 0
        while i < len(target):
            x = ord(target[i]) - ord('a')
            if count[x] == 0:
                break
            count[x] -= 1
            prefix.append(target[i])
            i += 1
        for j in range(i - 1, -1, -1):
            used = ord(prefix.pop()) - ord('a')
            count[used] += 1
            x = ord(target[j]) - ord('a')
            for c in range(x + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    answer = prefix + [chr(c + ord('a'))]
                    for k in range(26):
                        answer.extend(
                            [chr(k + ord('a'))] * count[k]
                        )
                    return "".join(answer)
        return ""