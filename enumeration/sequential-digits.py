class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        result = []

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result