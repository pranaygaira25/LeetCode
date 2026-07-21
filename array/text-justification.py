class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0

        while i < len(words):
            line_length = len(words[i])
            j = i + 1

            # Find how many words fit in one line
            while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(word) for word in line_words)
            spaces = maxWidth - total_chars

            # Last line or only one word -> left justified
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space_between = spaces // (num_words - 1)
                extra_spaces = spaces % (num_words - 1)

                line = ""
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += " " * (space_between + (1 if k < extra_spaces else 0))
                line += line_words[-1]

            result.append(line)
            i = j

        return result