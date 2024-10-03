def star_pattern(n, x, y, board):
    if n == 3:
        board[x][y] = '*'
        board[x+1][y] = '*'
        board[x+2][y] = '*'
        board[x][y+1] = '*'
        board[x+1][y+1] = ' '
        board[x+2][y+1] = '*'
        board[x][y+2] = '*'
        board[x+1][y+2] = '*'
        board[x+2][y+2] = '*'
        return
    
    size = n // 3

    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            star_pattern(size, x + i * size, y + j * size, board)

n = int(input())
board = [[' ' for _ in range(n)]for _ in range(n)]

star_pattern(n, 0, 0, board)

for row in board:
    print(''.join(row))