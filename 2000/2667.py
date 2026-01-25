import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        i, j = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                    count += 1
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)
