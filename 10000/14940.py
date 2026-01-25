import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start = (i, j)
            dist[i][j] = 0

queue = deque([start])
while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] != 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and dist[i][j] == -1:
            dist[i][j] = -1
        elif grid[i][j] == 0:
            dist[i][j] = 0

for row in dist:
    print(*row)
