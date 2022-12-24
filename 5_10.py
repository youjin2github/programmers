# 값 입력받기 
n,m = map(int, input().split())

# 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# dfs로 특정 노드 방문 뒤 연결 노드 방문!
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y] == 0:
        # 방문하지 않았으면 방문 처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(j):
        if dfs(i,j) == True:
            result += 1

print(result)