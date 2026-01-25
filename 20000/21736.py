import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)
            break

queue = deque([start])
visited[start[0]][start[1]] = True
count = 0

while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
                if graph[nx][ny] == 'P':
                    count += 1

print(count if count > 0 else 'TT')
