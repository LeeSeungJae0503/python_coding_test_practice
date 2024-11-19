def solution(board):
    if not board or not board[0]:
        return 0

    N = len(board)
    M = len(board[0])
    
    dp = [[0] * M for _ in range(N)]
    squares = []
    
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                size = dp[i][j]
                x1, y1 = i - size + 1, j - size + 1
                x2, y2 = i, j
                
                squares.append((size, x1, y1, x2, y2))
                
    if not squares:
        return 0
    
    squares.sort(reverse=True, key=lambda x: x[0])
    
    size1, x1_1, y1_1, x2_1, y2_1 = squares[0]
    
    return size1 * size1
