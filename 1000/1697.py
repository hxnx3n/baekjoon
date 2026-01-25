import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1] * 100001
queue = deque([n])
visited[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    for nx in (x-1, x+1, 2*x):
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            queue.append(nx)
