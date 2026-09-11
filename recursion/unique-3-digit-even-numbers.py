class Solution:
    def totalNumbers(self, digits):
        count = [0] * 10
        for d in digits:
            count[d] += 1

        ans = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = [0] * 10
            need[a] += 1
            need[b] += 1
            need[c] += 1

            valid = True
            for d in range(10):
                if need[d] > count[d]:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans