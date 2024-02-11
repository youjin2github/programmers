def dfs(land, i, j, n, m, visited):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(i, j)]
    size = 0
    columns_covered = set()  
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        size += 1
        columns_covered.add(y) 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))
    return size, columns_covered

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_in_column = [0] * m
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                oil_size, columns_covered = dfs(land, i, j, n, m, visited)
                for column in columns_covered: 
                    oil_in_column[column] += oil_size

    return max(oil_in_column)
