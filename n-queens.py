import copy


def get_queen_placements(column, chess_board, answer, left_row, upper_diagonal, lower_diagonal, n):
    if column == n:
        answer.append(copy.deepcopy(chess_board))
        return

    for row in range(n):
        if left_row[row] == 0 and upper_diagonal[n - 1 + column - row] == 0 and lower_diagonal[row + column] == 0:
            left_row[row] = 1
            upper_diagonal[n - 1 + column - row] = 1
            lower_diagonal[row + column] = 1
            chess_board[row][column] = 'Q'
            get_queen_placements(column + 1, chess_board, answer, left_row, upper_diagonal, lower_diagonal, n)
            left_row[row] = 0
            upper_diagonal[n - 1 + column - row] = 0
            lower_diagonal[row + column] = 0
            chess_board[row][column] = '.'


if __name__ == '__main__':
    n = 4
    answer = []
    left_row = [0] * n
    upper_diagonal = [0] * (2 * n - 1)
    lower_diagonal = [0] * (2 * n - 1)
    board = [['.'] * n for i in range(n)]
    get_queen_placements(0, board, answer, left_row, upper_diagonal, lower_diagonal, n)
    print(answer)
