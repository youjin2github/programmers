def solution(board, h, w):
    
    ## 사방 탐색 문제
    
    # 상하좌우 선언
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    count = 0
    
    for k in range(0,4):
        dr = dx[k] + h
        dc = dy[k] + w
        if 0 <= dr < len(board) and  0 <= dc < len(board) and board[h][w] == board[dr][dc]:
            count += 1

    return count