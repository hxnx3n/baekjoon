import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
v = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for adj in graph[node]:
        if not visited[adj]:
            visited[adj] = True
            queue.append(adj)
            count += 1

print(count)
