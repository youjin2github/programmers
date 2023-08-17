# 최단 경로를 찾는 문제 따라서 bfs문제 따라서 데크를 불러온다
from collections import deque

def solution(maps):
    # 가로 n
    n = len(maps)
    # 세로 m
    m = len(maps[0])
    
    # 이동할 방향 (동, 서, 남, 북)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # BFS를 위한 큐 초기화 (x,y,dist)인데 여기서 1,1이 시작점이고 1씩 증가하니까 dist = 1 이 된다
    queue = deque([(1, 1, 1)])
    
    # 큐가 비어있지 않은 동안 계속 반복문을 실행
    while queue:
        # 데크는 popleft이다
        x, y, dist = queue.popleft()
        # 상대 팀 진영에 도착한 경우
        if x == n and y == m :
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 범위를 벗어나거나 벽인 경우 다음 반복문을 실행
            if nx < 1 or nx > n or ny < 1 or ny > m or maps[nx-1][ny-1] == 0:
                continue
            
            # 해당 칸을 방문했음을 표시
            maps[nx-1][ny-1] = 0
            
            # 다음 위치와 거리를 큐에 추가
            queue.append((nx, ny, dist + 1))
    
    # 상대 팀 진영에 도착하지 못한 경우
    return -1