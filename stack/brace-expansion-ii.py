class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expr(i):
            result = set()
            while True:
                part, i = parse_term(i)
                result |= part
                if i < len(expression) and expression[i] == ',':
                    i += 1
                else:
                    break
            return result, i
        def parse_term(i):
            result = {""}
            while i < len(expression) and expression[i] not in "},":
                if expression[i] == '{':
                    part, i = parse_expr(i + 1)
                    i += 1
                else:
                    part = {expression[i]}
                    i += 1
                result = {
                    a + b
                    for a in result
                    for b in part
                }
            return result, i
        result, _ = parse_expr(0)
        return sorted(result)