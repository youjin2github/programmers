def solution(n):
    # 삼각형 구조를 먼저 만들기
    answer = [[0 for j in range(1,i+1)] for i in range(1,n+1)]

    # 좌표 문제이므로 x,y를 생성, 맨 처음은 아래로 내려감 
    x, y = -1, 0
    # 숫자는 1부터 시작 
    num = 1
    for i in range(n): # 방향
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1

    return sum(answer, [])