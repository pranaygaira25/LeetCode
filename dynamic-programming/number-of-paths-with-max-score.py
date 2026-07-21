class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)

        # dp_score[i][j] = max score from cell (i,j) to end
        # dp_count[i][j] = number of paths giving that max score
        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]

        # Start from E cell
        dp_score[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1

        # Fill from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best_score = -1
                ways = 0

                # Possible moves reverse-wise:
                # from down, right, diagonal-down-right
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]

                for x, y in directions:
                    if x < n and y < n and dp_count[x][y] > 0:
                        if dp_score[x][y] > best_score:
                            best_score = dp_score[x][y]
                            ways = dp_count[x][y]
                        elif dp_score[x][y] == best_score:
                            ways = (ways + dp_count[x][y]) % MOD

                if ways == 0:
                    continue

                cell_value = 0
                if board[i][j].isdigit():
                    cell_value = int(board[i][j])

                dp_score[i][j] = best_score + cell_value
                dp_count[i][j] = ways % MOD

        if dp_count[0][0] == 0:
            return [0, 0]

        return [dp_score[0][0] % MOD, dp_count[0][0] % MOD]