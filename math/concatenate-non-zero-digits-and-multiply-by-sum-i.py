class Solution(object):
    def sumAndMultiply(self, n):
        digits = []
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                digits.append(ch)
                digit_sum += int(ch)

        if not digits:
            return 0

        concatenated = int("".join(digits))
        return concatenated * digit_sum