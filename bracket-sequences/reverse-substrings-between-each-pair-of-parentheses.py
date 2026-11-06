class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        result = []
        i = 0
        direction = 1

        while 0 <= i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction = -direction
            else:
                result.append(s[i])

            i += direction

        return ''.join(result)